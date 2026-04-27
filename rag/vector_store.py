# rag/vector_store.py
import os
from langchain_community.vectorstores import FAISS
import pickle

class VectorStore:
    def __init__(self, vector_store_file="data/book_vectorstore.pkl"):
        self.file = vector_store_file
        self.store = None

    def build_store(self, embeddings, metadatas):
        self.store = FAISS.from_embeddings(embeddings, metadatas)
        os.makedirs(os.path.dirname(self.vector_store_file), exist_ok=True)
        with open(self.vector_store_file, "wb") as f:
            pickle.dump(self.store, f)

    # def save(self):
    #     with open(self.file, "wb") as f:
    #         pickle.dump(self.store, f)

    def load(self):
        with open(self.file, "rb") as f:
            self.store = pickle.load(f)