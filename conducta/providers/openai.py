"""OpenAI provider module."""

# Imports
from typing import Literal, Union

from conducta.core.credentials import Credentials
from conducta.core.logger import Logger

# Logger
logger = Logger(__name__, file_name="conducta.log")

# OpenAI constants
OpenAISupportedModelIds = Literal["gpt-3.5-turbo"]


# OpenAI credentials
class OpenAICredentials(Credentials):
    """Credentials for the OpenAI provider."""

    OPENAI_API_KEY: str
    OPENAI_API_SECRET_KEY: str


# GPT-3.5 Turbo model
class GPT35Turbo:
    """GPT-3.5 Turbo model class."""

    def call(self: "GPT35Turbo") -> None:
        """Call the GPT-3.5 Turbo model."""
        logger.debug("GPT-3.5 Turbo is calling")


# OpenAI provider
class OpenAI:
    """OpenAI provider class."""

    def __init__(self: "OpenAI") -> None:
        """Initialize the OpenAI provider and load the credentials."""
        self.credentials = OpenAICredentials()
        self.models = self.models(self)

    class models:
        """Models class for the OpenAI provider."""

        def __init__(self: "OpenAI", openai_instance: "OpenAI") -> None:
            """Initialize the models class."""
            self.openai_instance = openai_instance
            self.chat = self.chat(self.openai_instance)

        class chat:
            """Chat models class for the OpenAI provider."""

            def __init__(self: "OpenAI", openai_instance: "OpenAI") -> None:
                """Initialize the chat models class."""
                self.openai_instance = openai_instance

            def get(
                self: "OpenAI", model_id: OpenAISupportedModelIds
            ) -> Union[GPT35Turbo, None]:
                """Get the chat model by its ID."""
                if model_id == "gpt-3.5-turbo":
                    return GPT35Turbo()
                return None
