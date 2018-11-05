import os

from logzero import logger

from server import Server


class Pyromine:
    PATH = os.getcwd() + "/"
    DATA_PATH = os.getcwd() + "/"
    PLUGIN_PATH = DATA_PATH + "plugins"
    def __init__(self):
        try:
            Server(self.DATA_PATH, self.PLUGIN_PATH)
        except Exception as e:
            logger.error(e)
