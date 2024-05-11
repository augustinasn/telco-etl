import logging
from constants import *


def set_up_logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=LOGS_FP,
                        format="%(asctime)s %(levelname)-8s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO)
    return logger
