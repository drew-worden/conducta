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
    provider_name = self.__class__.__name__.split("Credentials")[0]
    logger.info(
        f"Loading credentials for the {provider_name} provider...",
    )
    current_dir_files = os.listdir(Path.cwd())
    env_file = [file for file in current_dir_files if file == ".env"]

    credentials = {}
    for cred in self.__annotations__:
        credentials[cred] = None

    # Load credentials from current environment
    if len(env_file) == 0:
        logger.warning(
            "No .env file found in current directory, looking in current environment..."
        )
        for cred in self.__annotations__:
            if os.getenv(cred):
                credentials[cred] = os.getenv(cred)
            else:
                msg = f"{cred} not found in current environment. Please add it to use the {provider_name} provider."
                logger.error(msg)
                raise ValueError(msg)
        logger.info(
            f"All {provider_name} credentials successfully loaded from the current environment."
        )
        return credentials

    # Load credentials from .env file
    logger.info(
        "A .env file was found in the current directory, loading credentials from the file..."
    )
    with Path(".env").open() as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("#"):
                continue
            parts = line.strip().split("=", 1)
            if parts[0] in credentials:
                credentials[parts[0]] = parts[1]

    # Check all credentials were loaded
    for cred in credentials:
        if not credentials[cred]:
            msg = f"{cred} not found in .env file. Please add it to use the {provider_name} provider."
            logger.error(msg)
            raise ValueError(msg)
    logger.info(
        f"All {provider_name} credentials successfully loaded from the .env file."
    )
    return credentials


class Credentials:
    """Base class for loading credentials for providers."""

    def __init__(self: "Credentials") -> None:
        """Initialize the Credentials class."""
        self.__credentials = self.__load_credentials_internal()
        for cred in self.__credentials:
            setattr(self, cred, self.__credentials[cred])

    def __load_credentials_internal(self: "Credentials") -> _lru_cache_wrapper:
        """Load credentials for the provider."""
        return load_credentials(self)
