import os
from langchain_community.vectorstores import FAISS


class VectorStore:
    def __init__(self, vector_store_file="data/book_vectorstore"):
        self.vector_store_file = vector_store_file
        self.store = None

    def build_store(self, texts, embedding_model, metadatas=None):
        """
        Build FAISS vector store from text documents.
        
        Args:
            texts (list[str]): Text chunks/documents
            embedding_model: HuggingFace embedding model instance
            metadatas (list[dict], optional): Metadata for each text
        """
        self.store = FAISS.from_texts(
            texts=texts,
            embedding=embedding_model,
            metadatas=metadatas
        )

        os.makedirs(os.path.dirname(self.vector_store_file), exist_ok=True)

        # Save FAISS properly
        self.store.save_local(self.vector_store_file)

    def load(self, embedding_model):
        """
        Load FAISS vector store from disk.
        """
        self.store = FAISS.load_local(
            self.vector_store_file,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return self.store