import os  # Operating system module for environment variable access
from dotenv import load_dotenv  # Function to load variables from .env file
import google.generativeai as genai  # Official Google Generative AI SDK
import numpy as np  # Numerical Python library for array vector operations

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Generate vector embedding for a given text input
def generate_embeddings(text):
    response = genai.embed_content(
        model="models/gemini-embedding-001",  # Standard Google text embedding model
        content=text 
    )
    return response['embedding']

# Calculate cosine similarity between two dimensional vectors
def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1) 
    vec2 = np.array(vec2)  
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) # Compute cosine angle score

base_text = "How do I reset my password?" 
similar_text = "Steps to change your login credentials" 
diff_text = "What's the weather today?"

emb_base = generate_embeddings(base_text)  # Generate vector for base query
emb_similar = generate_embeddings(similar_text)  # Generate vector for related text
emb_diff = generate_embeddings(diff_text)  # Generate vector for unrelated text

print(f"Similarity (password vs credentials): {cosine_similarity(emb_base, emb_similar):.3f}")  
print(f"Similarity (password vs weather): {cosine_similarity(emb_base, emb_diff):.3f}")