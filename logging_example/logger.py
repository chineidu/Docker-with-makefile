import typing as tp
import logging.config
from rich.logging import RichHandler
from pathlib import Path

def custom_logger():
    """This is used to create a custom logger that saves the output
    to the path: logs/

    Sample messages:
    ----------------
        logger.debug("Used for debugging your code.")
        logger.info("Informative messages from your code.")
        logger.warning("Everything works but there is something to be aware of.")
        logger.error("There's been a mistake with the process.")
        logger.critical("There is something terribly wrong and process may terminate.")

    """
    BASE_DIR = Path(__name__).absolute().parent
    LOGS_DIR = Path(BASE_DIR, "logs")
    # Create directory
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    # Use config file to initialize logger
    CONFIG_DIR = BASE_DIR
    logging.config.fileConfig(Path(CONFIG_DIR, "logging.config"))
    logger = logging.getLogger()
    logger.handlers[0] = RichHandler(markup=True)  # set rich handler
    return logger


def set_up_logger(delim: str = "::") -> tp.Any:
    """This is used to create a basic logger."""
    format_ = f"[%(levelname)s] {delim} %(asctime)s {delim} %(message)s"
    logging.basicConfig(level=logging.INFO, format=format_)
    logger = logging.getLogger(__name__)
    return logger


if __name__ == '__main__':
    logger = custom_logger()

    logger.debug("Used for debugging your code.")
    logger.info("Informative messages from your code.")
    logger.warning("Everything works but there is something to be aware of.")
    logger.error("There's been a mistake with the process.")
    logger.critical("There is something terribly wrong and process may terminate.")