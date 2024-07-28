# Imports
import os
from pathlib import Path
from functools import lru_cache
from conducta.core.logger import Logger

# Logger
logger = Logger(__name__, file_name="conducta.log")

class Credentials():
    def __init__(self):
        self.load_credentials()

    @lru_cache
    def load_credentials(self):
        logger.info(f"Loading credentials for the {self.__class__.__name__.split('Credentials')[0]} provider...")
        current_dir_files = os.listdir(os.getcwd())
        env_files = [file for file in current_dir_files if file.startswith('.env')]
        for cred in self.__annotations__:
            print(cred)