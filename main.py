"""Ejecuta la aplicación"""
from src.logger import logger
from src.view.views.app import App


def run():
    logger.debug(f"Iniciando main.run")
    app = App()
    app.mainloop()


if __name__ == "__main__":
    run()
