from src.view.components.conjunctInput import ConjunctInput
from src.view.components.conjunctOutput import ConjunctOutput
import ttkbootstrap as ttk
from src.model.models.conjunct import Conjunct
from src.view.components.window import Window
from typing import Callable


class ConjunctDisplay(ttk.Frame):
    def __init__(self, master, name: str, updateOutput: Callable):
        super().__init__(master)
        self.updateOutput = updateOutput
        self.conjunct = Conjunct(name=name)
        self.conjunctOutput = ConjunctOutput(self, conjunct=self.conjunct)
        self.conjunctInput = ConjunctInput(
            self, conjunct=self.conjunct, onGeneration=self.update
        )

        self.conjunctInput.pack()
        self.conjunctOutput.pack()

    def update(self):
        self.conjunctOutput.update()
        self.updateOutput()


if __name__ == "__main__":
    view = Window()
    component = ConjunctDisplay(view)
    component.pack()
    view.mainloop()
