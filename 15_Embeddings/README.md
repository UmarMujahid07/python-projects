# 15_Embeddings: Semantic Search & Cosine Similarity

A modular vector embeddings implementation built using **Google Generative AI SDK** (`google-generativeai`) and **NumPy**. This module demonstrates how to convert natural language text into high-dimensional numerical vectors, calculate pairwise cosine similarity scores, and build a basic semantic search engine to rank and retrieve documents based on conceptual relevance.

## Key Features

- **Dense Vector Representations**: Maps unstructured text into floating-point vector coordinates using `models/gemini-embedding-001` to capture semantic context.
- **Cosine Similarity Engine**: Implements vector distance math via NumPy (`np.dot` and `np.linalg.norm`) to measure geometric angles and closeness between text concepts.
- **Semantic Document Retrieval**: Queries a knowledge base by comparing search vectors against candidate document vectors rather than relying on exact keyword matches.
- **Document Score Ranking**: Sorts similarity results in descending order using custom lambda functions to surface the most contextually relevant documents.
- **Modular Script Architecture**: Separates basic pairwise similarity checks (`embedding_similarity.py`) from search retrieval logic (`semantic_search.py`) for clean code organization.

## Tech Stack

- **Language**: Python 3.x
- **SDK**: Google Generative AI (`google-generativeai`)
- **Math & Vector Operations**: NumPy (`numpy`)
- **Model**: Google Gemini Embeddings (`models/gemini-embedding-001`)
- **Configuration**: `python-dotenv`

## Project Structure

```text
15_Embeddings/
│
├── .env                    # Environment variables file containing GOOGLE_API_KEY (Git ignored)
├── .gitignore              # Git ignore rule file for workspace security
├── embedding_similarity.py # Script for pairwise concept similarity evaluation
├── semantic_search.py      # Script for document ranking and vector search retrieval
└── README.md               # Technical project documentation