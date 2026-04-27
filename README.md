#  Library RAG Chatbot

A domain-specific Retrieval-Augmented Generation (RAG) chatbot that enables users to interact with a library knowledge base using natural language.
This project integrates Neo4j Graph Database, HuggingFace Embeddings, FAISS Vector Search, Groq LLM, and Streamlit to create an intelligent assistant for semantic library information retrieval.

---

#  Project Overview

Traditional library systems rely on keyword search and structured filtering, which can be limiting for users seeking conversational or semantic discovery.

**Library RAG Chatbot** solves this by allowing users to ask questions like:

* “Suggest fantasy books with magic”
* “Who wrote historical fiction novels?”

The chatbot retrieves relevant information from a structured library database and generates contextual answers using an LLM.

---

#  Core Features

##  Natural Language Querying

Users can interact conversationally instead of using rigid search filters.

##  Neo4j Graph Database Integration

Stores interconnected entities like:

* Books
* Authors
* Genres
* Publishers
* Members
* Library Branches

##  Semantic Search with FAISS

Uses vector embeddings for meaning-based retrieval rather than exact keyword matching.

##  HuggingFace Embeddings

Transforms textual representations of library records into searchable vectors.

##  Groq LLM Integration

Uses **Llama 3.1 8B Instant** for fast and grounded AI-generated responses.

##  Streamlit Frontend

Provides an easy-to-use web-based chat interface.

---

#  System Architecture

```text
Neo4j Graph Database
        ↓
Data Loader (Cypher Queries)
        ↓
Node-to-Text Conversion
        ↓
HuggingFace Embeddings (E5-small)
        ↓
FAISS Vector Store
        ↓
Retriever
        ↓
Groq LLM (Llama 3.1)
        ↓
Streamlit Chat Interface
```

---

#  Technologies Used

## AI / Machine Learning

* Retrieval-Augmented Generation (RAG)
* HuggingFace `intfloat/e5-small`
* FAISS Vector Database
* Groq API
* Llama 3.1 8B Instant

## Backend

* Python
* LangChain
* Neo4j
* Cypher Query Language

## Frontend

* Streamlit

---

#  Installation & Setup

## 1️ Clone Repository

```bash
git clone https://github.com/mirdulaabalaji/Library-Chatbot-using-RAG.git
cd library-rag-chatbot
```

## 2️ Create Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows)

```bash
venv\Scripts\activate
```

## 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=your_neo4j_username
NEO4J_PASS=your_neo4j_password
GROQ_API_KEY=your_groq_api_key
```

---

#  Running the Project

```bash
streamlit run app/streamlit_app.py
```

---

#  Workflow Explanation

## Step 1: Neo4j Data Extraction

```cypher
MATCH (n) RETURN n
```

## Step 2: Data Preprocessing

Each node is converted into text for embedding.

## Step 3: Embedding Generation

Uses HuggingFace E5-small to generate semantic vectors.

## Step 4: FAISS Indexing

Stores vectors for fast similarity search.

## Step 5: Query Retrieval

User query → Embedding → Similarity Search → Relevant documents.

## Step 6: LLM Generation

Relevant documents are passed to Groq Llama 3.1 for grounded responses.

---

#  Example Query

**User:**

```text
Suggest mystery books with detectives
```

**Output:**

```text
Here are some detective-based mystery books in the library:
1. Sherlock Holmes
2. Murder on the Orient Express
```

---
