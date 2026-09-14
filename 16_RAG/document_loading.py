import os
# Import PDF reader class from PyPDF library
from pypdf import PdfReader

# Resolve absolute path to avoid missing file errors
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct target path for the PDF document
pdf_path = os.path.join(current_dir, "company_policy.pdf")

# Initialize PDF reader instance with target file
reader = PdfReader(pdf_path)
# Initialize empty string variable for extracted text
document_text = ""

# Loop through each page in the PDF document
for page in reader.pages:
    # Extract text from current page and append to string
    document_text += page.extract_text()

# Output total extracted character count to terminal
print(f"Total extracted characters: {len(document_text)}")