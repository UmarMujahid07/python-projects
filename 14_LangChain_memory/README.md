# 14_LangChain_Memory: Stateful Session-Isolated Chat Engine

A stateful, multi-session chat architecture built using **LangChain Expression Language (LCEL)**, **Google Gemini 3.6 Flash**, and `RunnableWithMessageHistory`. This module demonstrates how to wrap production LCEL chains with in-memory session management to maintain independent chat contexts across multiple users or interaction threads.

## Key Features

- **Stateful LCEL Integration**: Extends basic prompt-model pipelines with stateful conversation memory without hardcoding state inside prompt functions.
- **Dynamic Message Placeholders**: Employs `MessagesPlaceholder` to dynamically inject conversational context into the prompt structure.
- **Session-Isolated Context**: Tracks separate user sessions using custom `session_id` keys, ensuring complete context isolation between distinct users.
- **In-Memory Chat Storage**: Utilizes `InMemoryChatMessageHistory` to automatically track and update input/output message sequences (`HumanMessage` and `AIMessage`).
- **Clean Output Parsing**: Integrates `StrOutputParser` to handle string conversion directly at the end of the LCEL chain.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: LangChain (`langchain-core`, `langchain-google-genai`)
- **LLM**: Google Gemini 3.6 Flash (`gemini-3.6-flash`)
- **Configuration**: `python-dotenv`

## Project Structure

```text
14_LangChain_Memory/
│
├── main.py          # Primary application script implementing LCEL with session memory
├── .env             # Environment variables file containing API keys (Git ignored)
├── .gitignore       # Git ignore rule file for workspace security
└── README.md        # Technical documentation