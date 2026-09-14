import os
from pypdf import PdfReader

# Custom fixed-size character chunking algorithm with sliding window overlap
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        # Advance window forward while maintaining overlap boundary
        start += chunk_size - overlap
    return chunks

# Resolve absolute path to input PDF file
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "company_policy.pdf")

# Extract and aggregate plain text from all PDF pages
reader = PdfReader(pdf_path)
document_text = ""
for page in reader.pages:
    document_text += page.extract_text()

# Generate and inspect chunks
chunks = chunk_text(document_text)
print(f"Total chunks: {len(chunks)}")
print(chunks[0])