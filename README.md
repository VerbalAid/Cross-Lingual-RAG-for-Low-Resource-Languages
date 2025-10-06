# 🌍 Cross-Lingual RAG for Low-Resource Languages

A simple multilingual search system that finds relevant documents in Irish, French, and Spanish. Users can search in any language and get matching documents with similarity scores - no answer generation or translation involved.

## Quick Start

### Installation

**Python 3.10 or 3.11 required** (Python 3.13 not supported)

```bash
# Create environment
conda create -n rag_env python=3.11 -y
conda activate rag_env

# Install dependencies
pip install streamlit sentence-transformers torch scikit-learn numpy

# Run the app
streamlit run app.py
Then open http://localhost:8501 in your browser.

Example Queries
"Tell me about traditional music"

"Famous artists in Spain"

"Irish mythology"

How It Works
Documents in Irish, French and Spanish are stored in a dictionary

Embeddings created using paraphrase-multilingual-MiniLM-L12-v2

Search calculates cosine similarity between query and documents

Results show top matches with colour-coded relevance scores

Project Structure
text
├── app.py              # Main Streamlit app
├── README.md           # This file
└── requirements.txt    # Dependencies
Customisation
Change model: Swap paraphrase-multilingual-MiniLM-L12-v2 for other multilingual models

Adjust results: Modify top_k parameter in search function

Future ideas: Add FAISS, summarisation, or translation

Licence
MIT Licence

text

I've made it:
- **Shorter and more concise** - removed repetitive sections
- **Student-appropriate** - simpler language, less formal
- **British English** - "colour", "customisation", "licence"
- **Fixed formatting** - proper code block structure
- **Upload-ready** - clean markdown that will render correctly on GitHub

The tone is now more believable for a student project while keeping all essential information.
I want it to be a file
markdown
# 🌍 Cross-Lingual RAG for Low-Resource Languages

A simple multilingual search system that finds relevant documents in Irish, French, and Spanish. Search in any language and get matching documents with similarity scores.

## Quick Start

**Requires Python 3.10 or 3.11**

```bash
# Create environment
conda create -n rag_env python=3.11 -y
conda activate rag_env

# Install dependencies
pip install streamlit sentence-transformers torch scikit-learn numpy

# Run app
streamlit run app.py
Open http://localhost:8501 and try queries like:

"Traditional music"

"Spanish artists"

"Irish myths"

How It Works
Documents in 3 languages stored locally

paraphrase-multilingual-MiniLM-L12-v2 creates embeddings

Cosine similarity finds best matches

Results show with colour-coded scores

Project Structure
text
├── app.py
├── README.md
└── requirements.txt
Future Improvements
Add FAISS for faster search

Include more languages

Add result summarisation

Licence
MIT Licence
