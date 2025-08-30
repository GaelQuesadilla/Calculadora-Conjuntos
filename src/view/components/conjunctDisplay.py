from src.view.components.conjunctInput import ConjunctInput
from src.view.components.conjunctOutput import ConjunctOutput
import ttkbootstrap as ttk
from src.model.models.conjunct import Conjunct
from src.view.components.window import Window


class ConjunctDisplay(ttk.Frame):
    def __init__(self, master, name: str):
        super().__init__(master)
        self.conjunct = Conjunct(name=name)
        self.conjunctOutput = ConjunctOutput(self, conjunct=self.conjunct)
        self.conjunctInput = ConjunctInput(
            self, conjunct=self.conjunct, onGeneration=self.conjunctOutput.update
        )

        self.conjunctInput.pack()
        self.conjunctOutput.pack()


if __name__ == "__main__":
    view = Window()
    component = ConjunctDisplay(view)
    component.pack()
    view.mainloop()
