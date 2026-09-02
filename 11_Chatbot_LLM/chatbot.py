import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from local .env file
load_dotenv()

# Configure the Gemini API client using key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Generative Model instance
model = genai.GenerativeModel("gemini-3.6-flash")

# Initialize stateful conversation session
chat = model.start_chat(history=[])

print("Welcome to my chatbot..!\n")

# Start infinite conversation loop
while True:
    # Get user prompt from terminal
    user_input = input("You: ")

    # Exit condition check
    if user_input.lower() == "exit":
        print("Thank you for using chatbot..!")
        break

    try:
        # Send message within stateful chat session (persists history across turns)
        response = chat.send_message(user_input)
        print(f"AI: {response.text}\n")
    except Exception as e:
        # Catch and print any API/Network exceptions
        print(f"Error: {e}\n")

# NOTE: Stateful execution using chat.send_message() retains context across turns.
# Example interaction:
#   User: my name is Umar -> AI: Nice to meet you, Umar!
#   User: what's my name? -> AI: Your name is Umar.