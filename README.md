# Cross-Lingual RAG for Low-Resource Languages

A practical exploration of multilingual retrieval-augmented generation (RAG) systems, comparing performance across high-resource and low-resource languages.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Results Summary](#results-summary)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
  - [Installation](#installation)
  - [Build Database](#build-database)
  - [Run Interactive App](#run-interactive-app)
  - [Run Evaluation](#run-evaluation)
- [How It Works](#how-it-works)
  - [Document Processing](#document-processing)
  - [Retrieval Process](#retrieval-process)
  - [Evaluation Methodology](#evaluation-methodology)
- [Key Findings](#key-findings)
  - [Why the Performance Gap](#why-the-performance-gap)
  - [Implications](#implications)
- [Customization](#customization)
  - [Adding New Languages](#adding-new-languages)
  - [Using Your Own Documents](#using-your-own-documents)
  - [Changing Embedding Model](#changing-embedding-model)
- [Technical Notes](#technical-notes)
  - [Chunking Strategy](#chunking-strategy)
  - [FAISS Index Type](#faiss-index-type)
  - [Embedding Normalization](#embedding-normalization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Project Overview

This project tests the limits of cross-lingual RAG by querying in English and retrieving from documents in five languages:

**High-resource languages:**
- English
- French
- Spanish
- Portuguese

**Low-resource languages:**
- Irish

**Key Question:** Can a multilingual embedding model bridge the gap between high-resource and low-resource languages in retrieval tasks?

---

## Results Summary

Expected findings:

- **High-resource languages:** 85-95% retrieval accuracy
- **Low-resource languages:** 60-75% retrieval accuracy
- **Performance gap:** ~20 percentage points

This demonstrates the "resource curse" in NLP - low-resource languages consistently underperform due to limited training data.

---

## Architecture

```
User Query (English) 
    ↓
Multilingual Embedding Model
    ↓
Vector Search (FAISS)
    ↓
Retrieve from 5 Language Databases
    ↓
Display Results with Similarity Scores
```

**Tech Stack:**

- **Embeddings:** `paraphrase-multilingual-MiniLM-L12-v2` (sentence-transformers)
- **Vector Database:** FAISS (Facebook AI Similarity Search)
- **Interface:** Streamlit
- **Evaluation:** Custom metrics + visualization

---

## Project Structure

```
cross-lingual-rag/
├── data/                          # Source documents
│   ├── english/
│   │   ├── rlhf_notes.txt
│   │   ├── instruction_tuning_notes.txt
│   │   └── rag_notes.txt
│   ├── french/                    # Translated versions
│   ├── spanish/
│   ├── portuguese/
│   └── irish/
├── results/                       # Generated files (not in git)
│   ├── index_*.faiss             # Vector indices per language
│   ├── chunk_stores.pkl          # Document metadata
│   ├── accuracy_plot.png         # Performance visualization
│   └── *.csv                     # Evaluation results
├── build_database.py             # Create vector database
├── app.py                        # Streamlit interface
├── evaluate.py                   # Run evaluation suite
├── requirements.txt              # Python dependencies
└── README.md
```

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/cross-lingual-rag.git
cd cross-lingual-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Build Database

```bash
python build_database.py
```

This will:
- Load documents from `data/` folders
- Chunk text into overlapping segments
- Generate embeddings using multilingual model
- Create FAISS indices for each language
- Save to `results/` directory

### Run Interactive App

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501` and try queries like:
- "What is RLHF?"
- "How does instruction tuning work?"
- "Explain retrieval augmented generation"

### Run Evaluation

```bash
python evaluate.py
```

Generates:
- Retrieval accuracy per language
- High vs low-resource comparison
- Performance visualization (`accuracy_plot.png`)
- Detailed results (`detailed_results.csv`)

---

## How It Works

### Document Processing

1. Documents are split into ~300-word chunks with 50-word overlap
2. Each chunk is embedded into a 384-dimensional vector
3. Vectors are normalized and stored in FAISS indices

### Retrieval Process

1. User query (English) is embedded using same model
2. Cosine similarity search finds top-k most similar chunks per language
3. Results are ranked by similarity score
4. Sources are displayed with metadata

### Evaluation Methodology

- 10 test queries covering 3 topics (RLHF, Instruction Tuning, RAG)
- Success = correct topic retrieved in top-3 results
- Metrics: Accuracy, average similarity score, retrieval rank

---

## Key Findings

### Why the Performance Gap

**High-Resource Languages (French, Spanish, Portuguese):**

- ✓ Abundant training data in embedding model
- ✓ Rich linguistic resources
- ✓ Similar structure to English (Romance languages)

**Low-Resource Languages (Irish):**

- ✗ Limited training data
- ✗ Fewer digital resources
- ✗ Different linguistic structure (Celtic)

### Implications

Multilingual models show bias toward high-resource languages. Low-resource languages need specialized approaches:

- Language-specific fine-tuning
- Synthetic data generation
- Transfer learning from related languages
- Hybrid systems combining translation + retrieval

---

## Customization

### Adding New Languages

1. Create folder in `data/your_language/`
2. Add translated `.txt` files
3. Run `python build_database.py`

### Using Your Own Documents

1. Replace files in `data/english/` with your content
2. Translate to target languages
3. Rebuild database

### Changing Embedding Model

Edit `build_database.py` and `app.py`:

```python
# Try different models from sentence-transformers
model = SentenceTransformer("model-name-here")
```

**Options:**
- `paraphrase-multilingual-mpnet-base-v2` (larger, better quality)
- `distiluse-base-multilingual-cased-v2` (faster)
- `LaBSE` (Language-agnostic BERT sentence embeddings)

---

## Technical Notes

### Chunking Strategy

- **Size:** 300 words (~500 tokens)
- **Overlap:** 50 words (prevents boundary issues)
- **Why:** Balance between context and granularity

### FAISS Index Type

- **IndexFlatIP:** Inner product (cosine similarity after normalization)
- **Why:** Accurate, works well for small-to-medium datasets (<1M vectors)
- **Alternative:** Use `IndexIVFFlat` for larger datasets

### Embedding Normalization

```python
faiss.normalize_L2(embeddings)
```

Ensures cosine similarity = inner product, making scores comparable across languages.

---

## Contributing

Ideas for improvements:

- [ ] Add more languages (Arabic, Hindi, Swahili, etc.)
- [ ] Implement hybrid search (dense + sparse/BM25)
- [ ] Add reranking with cross-encoder
- [ ] Compare multiple embedding models
- [ ] Implement query translation as baseline
- [ ] Add support for multi-hop retrieval

---

## License

MIT License - feel free to use for research and education.

---

## Acknowledgments

- **sentence-transformers:** For multilingual embedding models
- **FAISS:** For efficient similarity search
- **Streamlit:** For rapid prototyping

---

## Contact

Questions or suggestions? Open an issue or reach out!

---

**Built with:** Python 3.8+ • sentence-transformers • FAISS • Streamlit
