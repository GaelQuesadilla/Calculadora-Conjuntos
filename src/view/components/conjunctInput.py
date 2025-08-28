from src.view.components.window import Window
import ttkbootstrap as ttk
from typing import List, Callable
from src.logger import logger
from src.model.models.conjunct import Conjunct
from ttkbootstrap.dialogs import Messagebox
from src.utils import functions


class conjunctInput(ttk.Frame):
    def __init__(
            self,
            master=None,
            conjunct=Conjunct(),
            onUpdate: Callable = lambda: logger.warning("Empty method")
    ):
        super().__init__(master)
        self.config(width=10)
        # ? Save values
        self.conjunct = conjunct
        self.onUpdate = onUpdate

        # ? Generate layout
        inputFrame = ttk.Frame(self)
        self.commandsFrame = ttk.Frame(self)
        self.functionFrame = ttk.Frame(inputFrame)
        self.valueFrame = ttk.Frame(inputFrame)

        # ? Pack
        inputFrame.pack(side=ttk.LEFT)
        self.commandsFrame.pack(side=ttk.LEFT)

        self.functionFrame.pack(pady=5, padx=5)
        self.valueFrame.pack(pady=5, padx=5)

        self._createComponents()

    def _createComponents(self):
        # ? Generate components

        self.runGeneratorButton = ttk.Button(
            self.commandsFrame,
            text="Generar",

            command=self._generateConjunct,
            style=ttk.SUCCESS)
        functionLabel = ttk.Label(self.functionFrame, text="f(x) = ")
        self.entryFunction = ttk.Entry(self.functionFrame)
        self.entryFunction.insert(0, "x**2")

        minLabel = ttk.Label(self.valueFrame, text="x_0 = ")
        self.entryMin = ttk.Entry(self.valueFrame, width=5)
        self.entryMin.insert(0, "0")

        maxLabel = ttk.Label(self.valueFrame, text="x_f = ")
        self.entryMax = ttk.Entry(self.valueFrame, width=5)
        self.entryMax.insert(0, "10")

        stepLabel = ttk.Label(self.valueFrame, text="p = ")
        self.entryStep = ttk.Entry(self.valueFrame, width=5)
        self.entryStep.insert(0, "1")

        # ? Pack components

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

        func_str = self.entryFunction.get()

        x_0_str = self.entryMin.get()
        x_f_str = self.entryMax.get()
        step_str = self.entryStep.get()

        if not func_str or not x_0_str or not x_0_str or not step_str:
            Messagebox.show_error(
                "No se cuenta con todos los valores para definir el conjunto")
            logger.error(
                f"No se cuenta con todos los valores para definir el conjunto")
            return

        try:

            def func(x): return eval(
                func_str,
                {"__builtins__": {}},
                {"x": x, "fibonacci": functions.fibonacci})

            x_0 = int(x_0_str)
            x_f = int(x_f_str)
            step = int(step_str)
            values: List[float] = [func(x) for x in range(x_0, x_f, step)]
            self.conjunct.values = set(values)
            self.onUpdate()

            logger.debug(f"Conjunto generado: {self.conjunct.values}")

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


if __name__ == "__main__":
    view = Window()
    component = conjunctInput(view)
    component.pack()
    view.mainloop()
