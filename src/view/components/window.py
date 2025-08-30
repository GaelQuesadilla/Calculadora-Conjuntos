from src.logger import logger
import ttkbootstrap as ttk


class Window(ttk.Window):
    def __init__(self, title="Calculadora de conjuntos", themename="superhero", iconphoto='', size=[1000, 550], position=None, minsize=None, maxsize=None, resizable=None, hdpi=True, scaling=None, transient=None, overrideredirect=False, alpha=1, **kwargs):
        super().__init__(title, themename, iconphoto, size, position, minsize, maxsize,
                         resizable, hdpi, scaling, transient, overrideredirect, alpha, **kwargs)


if __name__ == "__main__":
    view = Window()
    view.mainloop()
