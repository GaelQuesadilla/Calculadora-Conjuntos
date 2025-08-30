from src.view.components.window import Window
from src.view.components.conjunctDisplay import ConjunctDisplay
import ttkbootstrap as ttk
from typing import List
from src.view.components.conjunctOutput import ConjunctOutput
from src.model.models.conjunct import Conjunct


class App(Window):

    def __init__(self):

        super().__init__()

        self.container = ttk.Frame(self)
        self.container.pack(fill=ttk.BOTH, expand=True)

        self.leftFrame = ttk.Frame(self.container)
        self.rightFrame = ttk.Frame(self.container, style=ttk.DANGER)
        self.conjunctDisplays: List[ConjunctDisplay] = [self.createConjunctPack(name) for name in [
            "A", "B"]]

        self.keyboard = ttk.Frame(self.rightFrame)
        self.outputDisplay = ConjunctOutput(
            self.rightFrame, conjunct=Conjunct(name="Resultado")
        )

        # ? grid
        # ? Left frame

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=5)

        self.leftFrame.grid(row=0, column=0, sticky=ttk.NS)
        self.rightFrame.grid(row=0, column=1, sticky=ttk.NSEW)

        # ? Right frame
        self.rightFrame.grid_rowconfigure(0, weight=1)
        self.rightFrame.grid_columnconfigure(0, weight=1)
        self.rightFrame.grid_columnconfigure(1, weight=5)

        self.outputDisplay.grid(row=0, column=0, sticky=ttk.NSEW)
        self.keyboard.grid(row=1, column=0, sticky=ttk.NSEW)

        for conjunct in self.conjunctDisplays:
            conjunct.pack()

    def createConjunctPack(self, name: str):
        return ConjunctDisplay(self.leftFrame, name=name, updateOutput=self.updateOutput)

    def calcOutput(self):
        self.outputDisplay.conjunct = Conjunct(
            name="Result", values=self.conjunctDisplays[0].conjunct.values
        )

    def updateOutput(self):
        self.calcOutput()
        self.outputDisplay.update()
