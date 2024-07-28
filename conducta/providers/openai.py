# Imports
from typing import Literal
from conducta.core.credentials import Credentials

# OpenAI constants
OpenAISupportedModelIds = Literal["gpt-3.5-turbo"]

# OpenAI credentials
class OpenAICredentials(Credentials):
    OPENAI_API_KEY: str
    OPENAI_API_SECRET_KEY: str

# OpenAI provider
class OpenAI():
    def __init__(self):
        self.credentials = OpenAICredentials()
        self.models = self.models(self)
        
    class models:
        def __init__(self, openai_instance):
            self.openai_instance = openai_instance
            self.chat = self.chat(self.openai_instance)

        class chat:
            def __init__(self, openai_instance):
                self.openai_instance = openai_instance

            def get(self, model_id: OpenAISupportedModelIds):
                if model_id == "gpt-3.5-turbo":
                    return GPT35Turbo()
        
            
class GPT35Turbo():
    def call(self):
        print("GPT-3.5 Turbo is calling")