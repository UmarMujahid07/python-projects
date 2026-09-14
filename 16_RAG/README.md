# 16_RAG_Document_Ingestion

A foundational RAG (Retrieval-Augmented Generation) document processing module demonstrating text loading, manual fixed-size character chunking, and smart recursive text splitting for vector database readiness.

## Mini-Project Summary

| Script Name | Purpose | Key Techniques / Packages |
| :--- | :--- | :--- |
| **`01_document_loading.py`** | Raw text extraction from `.pdf` documents. | `pypdf`, absolute path resolution |
| **`02_manual_chunking.py`** | Fixed-size character chunking algorithm. | Sliding window mechanism, `chunk_overlap` |
| **`03_recursive_chunking.py`** | Context-aware recursive text splitting. | `langchain-text-splitters`, natural boundaries (`\n\n`, `\n`) |

---

## Key Concepts Explained

### 1. Why Chunking is Necessary
Raw documents cannot be directly indexed or sent to Large Language Models due to embedding accuracy limits and context window constraints. Chunking divides long documents into smaller, semantically focused context blocks.

### 2. Manual Sliding Window Chunking
Implements a strict character-count window (`chunk_size=500`) that steps forward while maintaining a tail overlap (`chunk_overlap=50`). It guarantees predictable chunk sizes but may slice words or sentences across boundaries.

### 3. Smart Recursive Chunking
`RecursiveCharacterTextSplitter` attempts to split text hierarchically using natural separators in order:
1. Double Newlines (`\n\n`) - Paragraphs
2. Single Newline (`\n`) - Sentences/Lines
3. Spaces (`" "`) - Words
4. Fallback Characters (`""`)

This preserves sentence integrity while enforcing token and character limits.

---

## How to Run

### Prerequisites
Ensure the necessary dependencies are installed in your virtual environment:

```bash
pip install pypdf langchain-text-splitters