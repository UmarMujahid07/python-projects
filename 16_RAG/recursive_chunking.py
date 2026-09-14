import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Resolve absolute path to input PDF file
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "company_policy.pdf")

# Extract and aggregate plain text from all PDF pages
reader = PdfReader(pdf_path)
document_text = ""
for page in reader.pages:
    document_text += page.extract_text()

# Smart text splitter prioritizing natural boundaries (\n\n, \n, space)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Generate and inspect chunks
chunks = splitter.split_text(document_text)
print(f"Total chunks: {len(chunks)}")
print(chunks[0])