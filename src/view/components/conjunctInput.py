from src.view.components.window import Window
import ttkbootstrap as ttk
from typing import List, Callable
from src.logger import logger
from src.model.models.conjunct import Conjunct
from ttkbootstrap.dialogs import Messagebox
from src.utils import functions


class ConjunctInput(ttk.Frame):
    def __init__(
            self,
            master=None,
            conjunct: Conjunct = Conjunct(),
            onGeneration: Callable = lambda: logger.warning("Empty method")):
        """Clase que define la forma de ingresar un conjunto. Contiene:
        f(x): Expresión matemática  [1,2,3,4]   x**2    x, x**2

        Parameters
        ----------
        master : optional
            Componente padre, by default None
        conjunct : Conjunct, optional
            Conjunto donde se almacenará el conjunto, by default Conjunct()
        onGeneration : Callable, optional
            Función que se ejecuta cuando se actualiza el conjunto, by default lambda:logger.warning("Empty method")
        """

        super().__init__(master)
        self.config(width=10)
        # ? Se guardan los valores
        self.conjunct = conjunct
        self.onGeneration = onGeneration

        # ? Título
        title = ttk.Label(self, text=f"Conjunto {conjunct.name}")
        # ? Se genera la estructura básica
        inputFrame = ttk.Frame(self)
        self.commandsFrame = ttk.Frame(self)
        self.functionFrame = ttk.Frame(inputFrame)
        self.valueFrame = ttk.Frame(inputFrame)

        # ? Se carga la estructura básica
        title.pack()
        inputFrame.pack(side=ttk.LEFT)
        self.commandsFrame.pack(side=ttk.LEFT)

        self.functionFrame.pack(pady=5, padx=5)
        self.valueFrame.pack(pady=5, padx=5)

        # ? Se generan los componentes
        # (Aquí está lo bueno)
        self._createComponents()

    def _createComponents(self):
        # ? Se generan los componentes

        # ? Botón generador
        self.runGeneratorButton = ttk.Button(
            self.commandsFrame,
            text="Generar",

            command=self._generateConjunct,
            style=ttk.SUCCESS)

        # ? Ingresa la expresión (por defecto x**2)
        functionLabel = ttk.Label(self.functionFrame, text="f(x) = ")
        self.entryFunction = ttk.Entry(self.functionFrame)
        self.entryFunction.insert(0, "x**2")

        # ?  Ingresa el valor mínimo de x (por defecto 0)
        minLabel = ttk.Label(self.valueFrame, text="x_0 = ")
        self.entryMin = ttk.Entry(self.valueFrame, width=5)
        self.entryMin.insert(0, "0")

        # ? Ingresa el valor máximo de x (por defecto 10)
        maxLabel = ttk.Label(self.valueFrame, text="x_f = ")
        self.entryMax = ttk.Entry(self.valueFrame, width=5)
        self.entryMax.insert(0, "10")

        # ? Ingresa el valor del paso (por defecto 1)
        stepLabel = ttk.Label(self.valueFrame, text="p = ")
        self.entryStep = ttk.Entry(self.valueFrame, width=5)
        self.entryStep.insert(0, "1")

        # ? Se cargan los componentes
        functionLabel.pack(pady=5, side=ttk.LEFT)
        self.entryFunction.pack()

        minLabel.pack(pady=10, side=ttk.LEFT)
        self.entryMin.pack(side=ttk.LEFT)

        maxLabel.pack(pady=10, side=ttk.LEFT)
        self.entryMax.pack(side=ttk.LEFT)

        stepLabel.pack(pady=10, side=ttk.LEFT)
        self.entryStep.pack(side=ttk.LEFT)

        self.runGeneratorButton.pack(pady=5)

    def _generateConjunct(self):
        """Mi parte favorita, está bien padre 🔥🔥🔥
        Genera el conjunto con la regla dada. Primero checa si es una lista, si no, ejecuta la expresión de x_0 a x_f
        De obtener un error muestra un cuadro de dialogo
        """
        func_str = self.entryFunction.get()

        # ? Se obtienen los datos como string
        x_0_str = self.entryMin.get()
        x_f_str = self.entryMax.get()
        step_str = self.entryStep.get()

        # ? Si no se cuenta con todos los valores muestra un cuadro de error y aborta
        if not func_str or not x_0_str or not x_f_str or not step_str:
            Messagebox.show_error(
                "No se cuenta con todos los valores para definir el conjunto")
            logger.error(
                f"No se cuenta con todos los valores para definir el conjunto")
            return

        try:
            # ? Intenta generar el conjunto

            # ? Define la función generadora y le da contexto
            def func(x: int): return eval(
                func_str,
                {"__builtins__": {}},
                {
                    "x": x,
                    "fibonacci": functions.fibonacci,
                    "par": functions.even,
                    "impar": functions.odd,
                    "div": functions.div,
                    "mult": functions.mult,
                    "potencia": functions.pow,
                }


            )

            # ? Convierte los datos ingresados a números enteros, si no funciona da error
            x_0 = int(x_0_str)
            x_f = int(x_f_str)
            step = int(step_str)

            try:
                # ? Evalúa la expresión, si es una lista la guarda
                evaluated = eval(
                    func_str,
                    {"__builtins__": {}})

                if not isinstance(evaluated, list):
                    raise TypeError

                logger.debug(f"Método ingresado de tipo lista")
                values = evaluated

            except Exception as e:
                # ? Si no funciona, intenta evaluar la función en el rango dado y guarda el resultado

                if callable(func):
                    logger.debug(f"Método ingresado de tipo función")
                    values: List[float] = [
                        func(x)for x in range(x_0, x_f, step)
                    ]

            self.conjunct.values = set(values)
            self.onGeneration()

            logger.debug(f"Conjunto generado: {self.conjunct.values}")

        # ? Si nada de esto funciona, se muestran cuadros de error dependiendo del error obtenido
        except ValueError as e:
            Messagebox.show_error(
                title="Error",
                message="No fue posible generar el conjunto\n"
                "Asegúrate de que los valores de las variables correspondan a números enteros")

            logger.error(
                f"Imposible definir f(x) = {func_str} en el rango [{x_0_str}, {x_f_str}]. Excepción: {e}"
            )

        except NameError as e:
            Messagebox.show_error(
                title="Error", message="No se encuentra la variable o función")

            logger.error(
                f"Imposible definir f(x) = {func_str} en el rango [{x_0_str}, {x_f_str}]. Excepción: {e}"
            )

        except Exception as e:
            Messagebox.show_error(
                title="Error", message="No fue posible generar el conjunto")

            logger.error(
                f"Imposible definir f(x) = {func_str} en el rango [{x_0_str}, {x_f_str}]. Excepción: {type(e)}: {e}"
            )
