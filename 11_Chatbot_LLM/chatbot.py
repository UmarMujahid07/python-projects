import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API client using key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Generative Model instance
model = genai.GenerativeModel("gemini-3.6-flash")

print("Welcome to my chatbot..!\n")

# Start infinite conversation loop
while True:
    # Get user prompt from terminal
    choice = input("You: ")

    # Exit condition check
    if choice.lower() == "exit":
        print("Thank you for using chatbot..!")
        break

    try:
        # Generate text response from LLM for single turn
        response = model.generate_content(choice)
        print(f"AI: {response.text}\n")
    except Exception as e:
        # Catch and print any API/Network exceptions
        print(f"Error: {e}\n")

# NOTE: For now this model can't remember anything (Stateless execution)
# Example interaction:
#   User: my name is Umar -> AI: nice to meet you umar!
#   User: what's my name ? -> AI: I can't have access to personal information