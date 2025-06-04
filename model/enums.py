"""
Enums for specific models to load and experiments to run
"""


from enum import Enum

class ModelType(Enum):
    hf_chat = 'hf_chat' # huggingface
    open_ai = 'open_ai' # OpenAI
    cohere = 'cohere' # Cohere
    anthropic = 'anthropic' # Anthropic