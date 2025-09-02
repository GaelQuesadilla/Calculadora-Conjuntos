import ttkbootstrap as ttk
from typing import Callable, Any, Optional
from src.logger import logger
from src.controller.controllers.operations import Operations


class Keyboard(ttk.Frame):
    """
    Keyboard simple con 6 botones definidos en el init.
    Cada botón al pulsarse guarda la operación en self.currentOption.
    """

    def __init__(
            self, master=None,
            onUpdateOperation: Callable = lambda: logger.warning(
                "onUpdateOperation Vacío")
    ):
        super().__init__(master)

        self.initializing = True
        self.onUpdateOperation = onUpdateOperation
        self._set_operation("Union A, B", self.union)

        self.unionBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Union A,B",
            command=lambda: self._set_operation("Union", self.union)
        )
        self.differenceBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Diferencia A,B",
            command=lambda: self._set_operation(
                "Diferencia A,B", self.difference)
        )
        self.intersectionBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Intersección A,B",
            command=lambda: self._set_operation(
                "intersection", self.intersection)
        )
        self.symmetricDifferenceBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Diferencia simétrica A,B",
            command=lambda: self._set_operation(
                "Diferencia simétrica A,B", self.symmetricDifference)
        )
        self.disjunctiveBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Disyuntiva A,B",
            command=lambda: self._set_operation(
                "Disyuntiva A,B", self.disjunctive)
        )
        self.symmetricProductBtn = ttk.Button(
            self,
            style=ttk.SECONDARY,
            text="Producto simetrico A,B",
            command=lambda: self._set_operation(
                "Producto simétrico A,B", self.symmetricProduct)
        )

        buttons = [
            self.unionBtn, self.differenceBtn, self.intersectionBtn,
            self.symmetricDifferenceBtn, self.disjunctiveBtn, self.symmetricProductBtn
        ]

        for i, btn in enumerate(buttons):
            r, c = divmod(i, 3)
            btn.grid(row=r, column=c, sticky=ttk.NSEW, padx=6, pady=6)

        for c in range(3):
            self.grid_columnconfigure(c, weight=1)
        for r in range(2):
            self.grid_rowconfigure(r, weight=1)

        self.initializing = False

    def _set_operation(self, label: str, operation: Callable[[Any, Any], Any]):
        self.label = label
        self.currentOption = operation

        if not self.onUpdateOperation:
            return
        if self.initializing:
            return

        self.onUpdateOperation()

    def currentOperation(self, A: Any, B: Any) -> Any:
        """
        Ejecuta la operación seleccionada sobre A y B.
        """
        if not self.currentOption:
            raise ValueError("No hay operación seleccionada.")
        return self.currentOption(A, B)

    def union(self, A, B):
        return Operations.union(A, B)

    def difference(self, A, B):
        return Operations.difference(A, B)

    def intersection(self, A, B):
        return Operations.intersection(A, B)

    def symmetricDifference(self, A, B):
        return Operations.symmetricDifference(A, B)

    def disjunctive(self, A, B):
        return Operations.disjunctive(A, B)

    def symmetricProduct(self, A, B):
        return Operations.symmetricProduct(A, B)
