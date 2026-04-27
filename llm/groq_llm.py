# llm/groq_llm.py
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, api_key: str):
        self.model = ChatGroq(
            api_key=api_key,
            model_name="llama-3.1-8b-instant")

    def get_model(self):
        return self.model