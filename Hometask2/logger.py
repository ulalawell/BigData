import logging


def get_module_logger(mod_name):
    """
                   Returns logger with selected configs

                   Parameters
                   ----------
                   mod_name: a name of module, where logger was called
    """
    logger = logging.getLogger(__name__)
    logger.setLevel('WARNING')

    formatter = logging.Formatter('%(asctime)s:%(module)s:%(funcName)s:%(levelname)s:%(message)s')

    file_handler = logging.FileHandler('data/info.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
