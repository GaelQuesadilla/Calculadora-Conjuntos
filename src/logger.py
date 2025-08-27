import logging
from pathlib import Path


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
