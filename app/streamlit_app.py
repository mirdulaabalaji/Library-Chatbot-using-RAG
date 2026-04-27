# app/streamlit_app.py
import os

# Use a simple, short Windows path to avoid long path issues
os.environ["HF_HOME"] = r"C:\Users\MirdulaaBalaji\.huggingface_cache"

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASS = os.getenv("NEO4J_PASS")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Import project modules
from database.neo4j_loader import Neo4jLoader
from rag.embeddings import EmbeddingsGenerator
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from llm.groq_llm import GroqLLM
from utils.helpers import node_to_text

# ---------------------
# Initialize Neo4j and fetch nodes
# ---------------------
@st.cache_data(show_spinner=True)
def load_nodes():
    loader = Neo4jLoader(NEO4J_URI, NEO4J_USER, NEO4J_PASS)
    nodes = loader.fetch_nodes()
    loader.close()
    return nodes

nodes = load_nodes()

# Convert nodes to text
documents = [{"text": node_to_text(n), "metadata": dict(n)} for n in nodes]
texts = [doc["text"] for doc in documents]
metadatas = [doc["metadata"] for doc in documents]

# ---------------------
# Initialize embeddings
# ---------------------
@st.cache_resource(show_spinner=True)
def init_embeddings():
    return EmbeddingsGenerator()

emb_gen = init_embeddings()
embeddings = emb_gen.generate_embeddings(texts)

# ---------------------
# Build / load FAISS vector store
# ---------------------
VECTOR_STORE_FILE = "data/book_vectorstore.pkl"

@st.cache_resource(show_spinner=True)
def init_vector_store():
    vs = VectorStore(vector_store_file=VECTOR_STORE_FILE)
    if os.path.exists(VECTOR_STORE_FILE):
        vs.load()
    else:
        vs.build_store(embeddings, metadatas)
    return vs

vector_store = init_vector_store()

# ---------------------
# Retriever
# ---------------------
retriever = Retriever(vector_store)

# ---------------------
# Groq LLM
# ---------------------
llm = GroqLLM(api_key=GROQ_API_KEY).get_model()

# ---------------------
# Streamlit UI
# ---------------------
st.set_page_config(page_title="Library RAG Chatbot", page_icon="📚")
st.title("📚 Library RAG Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask a question about your library:")

if st.button("Send") and query:
    # Retrieve relevant documents
    docs = retriever.get_relevant_documents(query)
    context_text = "\n".join([doc.page_content for doc in docs])

    # Prepare prompt for Groq
    prompt = f"""
You are a helpful librarian assistant. Use the following context to answer the question.

Context:
{context_text}

Question: {query}
Answer:
"""

    # Get answer from Groq LLM
    response = llm.predict(prompt)

    # Update chat history
    st.session_state.chat_history.append({"user": query, "bot": response})

# Display chat
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")