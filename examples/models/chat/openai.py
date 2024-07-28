"""Example use of the OpenAI chat model."""

# Imports
from conducta.providers.openai import OpenAI

# Instantiate the OpenAI provider
openai = OpenAI()

# Get the model by its ID
model = openai.models.chat.get("gpt-3.5-turbo")

# Call the model
model.call()
