import os 
import numpy as np
from dotenv import load_dotenv  
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Compute cosine similarity between two numeric vectors
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) 

# Generate embedding vector using Gemini embedding model
def generate_embedding(text):
    response = genai.embed_content(
        model="models/gemini-embedding-001",  # Google's text-embedding model
        content=text 
    )
    return response['embedding']  # Extract embedding vector array

documents = [  # List of target knowledge base document strings
    "How do I reset my password?",
    "What are your business hours?",
    "Steps to change your login credentials",
    "Where is your office located?"
]

query = "I forgot my login info"  # User natural language input query

query_embedding = generate_embedding(query)  # Convert user query string to embedding vector

# Empty list to hold document text and similarity score tuples
similarities = [] 
for doc in documents:  
    doc_embedding = generate_embedding(doc)  # Generate vector for current document
    similarity = cosine_similarity(query_embedding, doc_embedding)  # Compute similarity against query vector
    similarities.append((doc, similarity))  # Append document text and score tuple to results list

similarities.sort(key=lambda x: x[1], reverse=True)  # Sort results descending based on score value

print(f"Most relevant document: {similarities[0][0]}")  # Print top-ranked document text
print(f"Similarity score: {similarities[0][1]:.3f}")  # Print top-ranked document score