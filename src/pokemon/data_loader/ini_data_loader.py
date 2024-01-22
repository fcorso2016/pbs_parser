from configparser import ConfigParser
import pathlib

class IniDataLoader:
    def __init__(self, filename: str):
        self.config = ConfigParser()
        self.config.read(pathlib.Path(__file__).parent.absolute() / filename)
