# Imports
from typing import Literal

# Constants
OpenAISupportedModelIds = Literal["gpt-3.5-turbo"]

# OpenAI provider
class OpenAI():
    class models:
        class chat:
            @staticmethod
            def get(model_id: OpenAISupportedModelIds):
                if model_id == "gpt-3.5-turbo":
                    return GPT35Turbo()
            
class GPT35Turbo():
    def call(self):
        print("GPT-3.5 Turbo is calling")