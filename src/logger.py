import logging
from constants import *


def set_up_logger():
    """
    Sets up a logger for the application.

    Returns:
        logging.Logger: The configured logger object.

    Note:
        The logger is configured to write log messages to the file specified
        in the constant LOGS_FP with a specific format and logging level.
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=LOGS_FP,
                        format="%(asctime)s %(levelname)-8s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO)
    return logger
