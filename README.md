# 🌍 Cross-Lingual RAG for Low-Resource Languages

A practical exploration of multilingual retrieval-augmented search across Irish, French, and Spanish documents. This project allows users to search in any language and retrieve relevant documents with similarity scores. It does not generate answers or translate content.

## Table of Contents
- [Project Overview](#project-overview)
- [Current Functionality](#current-functionality)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Customisation](#customisation)
- [Licence](#licence)

## Project Overview

This project demonstrates a multilingual retrieval system that searches across Irish, French, and Spanish documents. Users can enter queries in any language and retrieve documents ranked by relevance.

**Key Notes:**
- The system retrieves documents, not answers
- Similarity scores show how closely each document matches the query
- No answer generation or translation performed

## Current Functionality

- 🔍 Search across Irish, French, and Spanish documents
- 📊 Return the top-k most relevant documents with cosine similarity scores
- 🎨 Colour-coded relevance indicator:
  - **Green**: Highly relevant (>0.7)
  - **Orange**: Moderately relevant (0.4-0.7)
  - **Red**: Low relevance (<0.4)
- 📄 Raw document content displayed without modification

## Quick Start

### Installation

⚠️ **Important**: Requires Python 3.11 or 3.10 due to dependency compatibility.

```bash
# Create environment
conda create -n rag_env python=3.11 -y
conda activate rag_env

# Install dependencies
pip install streamlit sentence-transformers torch scikit-learn numpy

# Run the app
streamlit run app.py
```

### Usage

1. Open `http://localhost:8501` in your browser
2. Enter a query in any language
3. View retrieved documents with relevance scores

**Example queries:**
* "Tell me about traditional music"
* "Famous artists in Spain"
* "Irish mythology"

## How It Works

1. **Document Collection**: Documents stored in a Python dictionary
2. **Embeddings**: Uses `paraphrase-multilingual-MiniLM-L12-v2` to convert text to vectors
3. **Search Process**:
   * Query is embedded into vector space
   * Cosine similarity calculated against all documents
   * Top-k matches returned with scores
4. **Display**: Results shown in Streamlit with coloured relevance indicators

## Project Structure

```
cross-lingual-rag/
├── app.py              # Streamlit interface
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Customisation

**Change Embedding Model:** Replace `SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')` with:
* `SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")` - More accurate
* `SentenceTransformer("distiluse-base-multilingual-cased-v2")` - Faster

**Adjust Results:** Modify the `top_k` parameter in the `search()` function.

**Ideas for Improvement:**
* Add FAISS for scalable similarity search
* Implement result summarisation
* Include more languages

## Licence

MIT Licence - free for educational use.

## Acknowledgements

* **sentence-transformers** for multilingual embeddings
* **Streamlit** for the web interface
* **PyTorch** for deep learning backend
