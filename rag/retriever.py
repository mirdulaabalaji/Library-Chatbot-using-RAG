# rag/retriever.py
class Retriever:
    def __init__(self, vector_store, k=5):
        self.vector_store = vector_store
        self.k = k

    def get_retriever(self):
        return self.vector_store.store.as_retriever(search_kwargs={"k": self.k})
    
    def get_relevant_documents(self, query):
        retriever = self.get_retriever()
        return retriever.get_relevant_documents(query)