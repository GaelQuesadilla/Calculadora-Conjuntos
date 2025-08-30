import tkinter as ttk
import ttkbootstrap as ttk
from src.model.models.conjunct import Conjunct
from src.view.components.window import Window


class ConjunctOutput(ttk.Frame):

    def __init__(self, master=None, conjunct=Conjunct()):
        super().__init__(master)
        self.conjunct = conjunct

        box_frame = ttk.Frame(self, relief=ttk.SOLID, padding=3)
        box_frame.pack(fill=ttk.X, expand=True)

        self._text = ttk.Text(
            box_frame, width=30)

        self._text.pack(side=ttk.LEFT, fill=ttk.X, expand=True)

        self.update()

    def update(self):
        """Refresca el texto con los valores actuales del conjunto."""
        values = getattr(self.conjunct, "values", None)
        if values is None:
            display = "(sin valores)"
        else:
            try:
                sorted_vals = sorted(values)
                display_lines = [f"{v:g}" for v in sorted_vals]
                display = ", ".join(
                    display_lines) if display_lines else "(conjunto vacío)"
            except Exception:
                display = str(values)

        self._text.configure(state="normal", height=3)
        self._text.delete("1.0", ttk.END)
        self._text.insert(ttk.END, display)
        self._text.configure(state="disabled")


if __name__ == "__main__":
    view = Window()
    conj = Conjunct(values=set([x for x in range(100)]))
    component = ConjunctOutput(view, conj)
    component.pack()
    view.mainloop()
