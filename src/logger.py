import logging
from pathlib import Path

"""Módulo para guardar los datos del sistema, permite al desarrollador depurar el código de manera mas sencilla y ordenada
"""


def setup_logger(logsDir: str, loggerName: str) -> logging.Logger:
    logsDir.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(
                logsDir / "logs.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logger: logging.Logger = logging.getLogger(loggerName)
    return logger


logger = setup_logger(
    logsDir=Path.cwd(),
    loggerName="App"
)
