import os
from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from local env file
load_dotenv()

# Initialize the Gemini chat model with API parameters
language_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize standard output parser to convert model responses into plain strings
output_parser = StrOutputParser()

# Define prompt template with system role, chat history placeholder, and user input slot
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Construct base processing chain
base_chat_chain = chat_prompt_template | language_model | output_parser

# Dictionary store to maintain chat history across multiple sessions
session_history_store = {}


# Function to retrieve or initialize session chat history
def get_session_history(session_id: str):
    if session_id not in session_history_store:
        session_history_store[session_id] = InMemoryChatMessageHistory()
    return session_history_store[session_id]


# Wrap base chain with session history management
chain_with_memory = RunnableWithMessageHistory(
    base_chat_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Primary interaction for session user1
first_user_response = chain_with_memory.invoke(
    {"input": "My name is Umar"},
    config={"configurable": {"session_id": "user1"}}
)
print(first_user_response)

# Secondary interaction for session user1 confirming history persistence
second_user_response = chain_with_memory.invoke(
    {"input": "what is my name?"},
    config={"configurable": {"session_id": "user1"}}
)
print(second_user_response)

# Interaction for isolated session user2 confirming session isolation
isolated_user_response = chain_with_memory.invoke(
    {"input": "what is my name?"},
    config={"configurable": {"session_id": "user2"}}
)
print(isolated_user_response)