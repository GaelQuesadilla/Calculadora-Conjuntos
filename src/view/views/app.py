from src.view.components.window import Window
from src.view.components.conjunctDisplay import ConjunctDisplay
import ttkbootstrap as ttk
from typing import List


class App(Window):

    def __init__(self):

        super().__init__()

        self.container = ttk.Frame(self)
        self.container.pack(fill=ttk.BOTH, expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=5)

        self.leftFrame = ttk.Frame(self.container)
        self.rightFrame = ttk.Frame(self.container, style=ttk.DANGER)
        conjunctDisplays = [self.createConjunctPack(name) for name in [
            "A", "B"]]

        # ? grid

        self.leftFrame.grid(row=0, column=0, sticky=ttk.NS)
        self.rightFrame.grid(row=0, column=1, sticky=ttk.NSEW)
        for conjunct in conjunctDisplays:
            conjunct.pack()

    def createConjunctPack(self, name: str):
        return ConjunctDisplay(self.leftFrame, name=name)
