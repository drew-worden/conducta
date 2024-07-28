"""Logger module for the project."""

# Imports
import copy
import logging
from logging import LogRecord
from typing import ClassVar, Optional


class ColorFormatter(logging.Formatter):
    """Logging formatter that adds color to the log messages that stream to stdout."""

    COLOR_CODES: ClassVar = {
        "DEBUG": "\033[90m",  # Gray
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    }
    RESET_CODE = "\033[0m"

    def format(self, record: LogRecord) -> str:
        """Format the log record with color."""
        colored_record = copy.copy(record)
        levelname = colored_record.levelname
        log_color = self.COLOR_CODES.get(levelname, self.RESET_CODE)
        colored_record.msg = f"{log_color}{colored_record.msg}{self.RESET_CODE}"
        return super().format(colored_record)


# Global formatters
COLOR_FORMATTER = ColorFormatter(
    "[%(asctime)s][%(levelname)s][%(name)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
NON_COLOR_FORMATTER = logging.Formatter(
    "[%(asctime)s][%(levelname)s][%(name)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Global handlers
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(COLOR_FORMATTER)


class Logger:
    """Logger class for the project. Should be instantiated with the name of the module, in every file."""

    def __init__(
        self: "Logger",
        name: str,
        level: int = logging.INFO,
        file_name: Optional[str] = None,
    ) -> None:
        """Initialize the logger with the name of the module."""
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(level)
            self.logger.addHandler(STREAM_HANDLER)

            if file_name:
                file_handler = logging.FileHandler(filename=file_name)
                file_handler.setFormatter(NON_COLOR_FORMATTER)
                self.logger.addHandler(file_handler)

    def info(self: "Logger", message: str) -> None:
        """Log an info message."""
        self.logger.info(message)

    def error(self: "Logger", message: str) -> None:
        """Log an error message."""
        self.logger.error(message)

    def warning(self: "Logger", message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)

    def debug(self: "Logger", message: str) -> None:
        """Log a debug message."""
        self.logger.debug(message)
