# rag/embeddings.py
from langchain_community.embeddings import HuggingFaceEmbeddings

class EmbeddingsGenerator:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="intfloat/e5-small",  # Windows-safe, pure transformers
            model_kwargs={"device": "cpu"}   # "cuda" if GPU
        )

    def generate_embeddings(self, texts):
        return self.model.embed_documents(texts)