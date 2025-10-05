# Cross-Lingual-RAG-for-Low-Resource-Languages
## Overview
This project demonstrates the performance gap between high-resource and low-resource languages in cross-lingual retrieval systems.

## Results
- **French**: 82% retrieval accuracy
- **Spanish**: 79% retrieval accuracy  
- **Portuguese**: 76% retrieval accuracy
- **Irish**: 43% retrieval accuracy

## Key Findings
1. Romance languages benefit from abundant training data
2. Irish suffers from limited multilingual model exposure
3. Technical terminology retrieval particularly challenging for Irish

## Repository Structure
- `data/` - Raw and processed documents
- `src/` - Core RAG system code
- `notebooks/` - Analysis and experimentation
- `results/` - Evaluation outputs and visualizations

## Setup
```bash
pip install -r requirements.txt
python -m jupyter notebook
