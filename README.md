# 🌍 Cross-Lingual RAG for Low-Resource Languages

A practical exploration of multilingual retrieval-augmented search across Irish, French, and Spanish documents. This project allows users to search in any language and retrieve the most semantically relevant documents, displayed with a similarity score. It does not generate answers or translate content.

## Table of Contents
- [Project Overview](#project-overview)
- [Current Functionality](#current-functionality)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Customisation](#customisation)
- [Contributing](#contributing)
- [License](#licence)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project demonstrates a multilingual retrieval system (SimpleRAG) that searches across Irish, French, and Spanish documents. Users can enter queries in any language and retrieve documents ranked by relevance.

**Key Notes:**
- The system retrieves documents, not answers
- Similarity scores show how closely each document matches the query
- Queries in English do not automatically produce English summaries

## Current Functionality

- 🔍 Search across Irish, French, and Spanish documents
- 📊 Return the top-k most relevant documents with cosine similarity scores
- 🎨 Colour-coded relevance indicator for quick reference:
  - **Green**: Highly relevant (>0.7)
  - **Orange**: Moderately relevant (0.4-0.7)
  - **Red**: Low relevance (<0.4)
- 📄 No answer generation or translation—raw document content is displayed

## Quick Start

### Installation & Python Fix

⚠️ **Important**: This app requires Python 3.11 or 3.10 due to compatibility issues with PyTorch and SentenceTransformers. Python 3.13 is not supported and will cause errors.

**Steps (recommended):**

1. Create a new environment:
```bash
conda create -n rag_env python=3.11 -y
conda activate rag_env

Run Interactive App
Open the app in your browser (default: http://localhost:8501)

Enter a query in any language, for example:

Tell me about traditional music

Famous artists in Spain

Irish mythology

View top-k retrieved documents with relevance scores

How It Works
Document Collection: Documents in Irish, French, and Spanish are stored in a Python dictionary

Embeddings: Uses paraphrase-multilingual-MiniLM-L12-v2 from sentence-transformers to convert documents and queries into dense vectors

Search Process:

Query is embedded

Cosine similarity is calculated against all document embeddings

Top-k matches are returned with similarity scores

Display: Results shown in Streamlit with coloured relevance scores

No translation or summarisation is performed

Project Structure
text
cross-lingual-rag/
├── app.py                     # Streamlit interface
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── data/                      # Document storage (optional expansion)
│   ├── irish/
│   ├── french/
│   └── spanish/
└── results/                   # Optional: cached embeddings (if you add caching)
Customisation
Change Embedding Model:
Replace SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2') with another multilingual model.

Examples:

SentenceTransformer("paraphrase-multilingual-mpnet-base-v2") - Larger, more accurate

SentenceTransformer("distiluse-base-multilingual-cased-v2") - Faster

Adjust top-k results:
Modify the top_k parameter in the search() function.

Ideas for improvement:

Implement result summarisation or translation

Introduce FAISS indexing for scalability

Add query reranking using cross-encoders

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions and improvements.

Licence
MIT Licence – free to use for research and education.

Acknowledgements
sentence-transformers: Multilingual embedding models

Streamlit: Interactive web interface

PyTorch: Deep learning backend
2. Install dependencies:
pip install streamlit sentence-transformers torch scikit-learn numpy

3. Run the app:
python -m streamlit run app.py

