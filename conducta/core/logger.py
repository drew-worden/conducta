########################################################################################
# FILE: logger.py                                                                      #
# DESCRIPTION: This file contains the logger class and the color formatter classes.    #
########################################################################################

########################################################################################
# IMPORTS                                                                              #
########################################################################################
from logging import LogRecord
import logging
import copy

########################################################################################
# COLOR FORMATTER FOR RENDERING COLOR LOGS STREAMED TO STDOUT                          #
########################################################################################
class ColorFormatter(logging.Formatter):

    COLOR_CODES = {
        'DEBUG': '\033[90m',    # Gray
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[95m'  # Magenta
    }
    RESET_CODE = '\033[0m'

    def format(self, record: LogRecord) -> str:
            """
            Formats the log record with color based on the log level.

            Args:
                record (LogRecord): The log record to be formatted.

            Returns:
                str: The formatted log message with color.

            """
            colored_record = copy.copy(record)
            levelname = colored_record.levelname
            log_color = self.COLOR_CODES.get(levelname, self.RESET_CODE)
            colored_record.msg = f"{log_color}{colored_record.msg}{self.RESET_CODE}"
            return super().format(colored_record)

########################################################################################
# GLOBAL LOGGING FORMATTER AND HANDLERS                                                #
########################################################################################

# Global formatters
COLOR_FORMATTER = ColorFormatter('[%(asctime)s][%(levelname)s][%(name)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
NON_COLOR_FORMATTER = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Global handlers
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(COLOR_FORMATTER)

########################################################################################
# LOGGER CLASS FOR LOGGING MESSAGES TO STDOUT AND LOG FILES. MEANT TO BE INITIALIZED   #
# IN EVERY FILE. DEFAULT BEHAVIOR IS TO JUST STREAM TO STDOUT UNLESS A FILE NAME IS    #
# PROVIDED                                                                             #
########################################################################################
class Logger:
    def __init__(self, name: str, level: int = logging.INFO, file_name: str = None):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(level)
            self.logger.addHandler(STREAM_HANDLER)

            if file_name:
                file_handler = logging.FileHandler(filename=file_name)
                file_handler.setFormatter(NON_COLOR_FORMATTER)
                self.logger.addHandler(file_handler)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)