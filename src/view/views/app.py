from src.view.components.window import Window
from src.view.components.conjunctDisplay import ConjunctDisplay
import ttkbootstrap as ttk
from typing import List
from src.view.components.conjunctOutput import ConjunctOutput
from src.model.models.conjunct import Conjunct
from src.view.components.keyboard import Keyboard
from ttkbootstrap.dialogs import Messagebox


class App(Window):

    def __init__(self):

        super().__init__()

        self.container = ttk.Frame(self)
        self.container.pack(fill=ttk.BOTH, expand=True)

        self.leftFrame = ttk.Frame(self.container)
        self.rightFrame = ttk.Frame(self.container)
        self.conjunctDisplays: List[ConjunctDisplay] = [self.createConjunctPack(name) for name in [
            "A", "B"]]

        self.keyboard = Keyboard(
            self.rightFrame, onUpdateOperation=self.updateOutput)
        self.outputDisplay = ConjunctOutput(
            self.rightFrame, conjunct=Conjunct(name="Resultado")
        )
        self.resultLabel = ttk.Label(self.rightFrame, text=self.keyboard.label)

        # ? grid

        # ? Left frame
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=5)

        self.leftFrame.grid(row=0, column=0, sticky=ttk.NS)
        self.rightFrame.grid(row=0, column=1, sticky=ttk.NSEW, padx=5)

        for conjunct in self.conjunctDisplays:
            conjunct.pack()

        # ? Right frame
        self.rightFrame.grid_columnconfigure(0, weight=1)
        self.rightFrame.grid_rowconfigure(0, weight=1)
        self.rightFrame.grid_rowconfigure(1, weight=19)
        self.rightFrame.grid_rowconfigure(2, weight=100)

        self.resultLabel.grid(row=0, column=0, sticky=ttk.EW)
        self.outputDisplay.grid(row=1, column=0, sticky=ttk.NSEW)
        self.keyboard.grid(row=2, column=0, sticky=ttk.NSEW)

    def createConjunctPack(self, name: str):
        return ConjunctDisplay(self.leftFrame, name=name, updateOutput=self.updateOutput)

    def calcOutput(self):
        try:
            self.outputDisplay.conjunct = self.keyboard.currentOperation(
                self.conjunctDisplays[0].conjunct,
                self.conjunctDisplays[1].conjunct,)

        except Exception as e:
            Messagebox.show_error(
                title="Error",
                message=f"Error inesperado calculando el conjunto\nExcepción{e}"
            )

    def updateLabel(self):
        self.resultLabel.config(text=self.keyboard.label)

    def updateOutput(self):
        self.calcOutput()
        self.updateLabel()
        self.outputDisplay.update()
