"""Loads and caches credentials for providers from local environment or .env files."""

# Imports
import os
from functools import _lru_cache_wrapper, lru_cache
from pathlib import Path

from conducta.core.logger import Logger

# Logger
logger = Logger(__name__, file_name="conducta.log")

@lru_cache
def load_credentials(self: "Credentials") -> None:
    """Load credentials from local environment or .env files for specific provider."""
    logger.info(
        f"Loading credentials for the {self.__class__.__name__.split('Credentials')[0]} provider...",
    )
    current_dir_files = os.listdir(Path.cwd())
    env_files = [file for file in current_dir_files if file.startswith(".env")]
    logger.debug(env_files)
    for cred in self.__annotations__:
        logger.debug(cred)


class Credentials:
    """Base class for loading credentials for providers."""

    def __init__(self: "Credentials") -> None:
        """Initialize the Credentials class."""
        self.load_credentials_internal()

    def load_credentials_internal(self: "Credentials") -> _lru_cache_wrapper:
        """Load credentials for the provider."""
        return load_credentials(self)
