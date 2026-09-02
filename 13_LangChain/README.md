# 13_LangChain: Sequential Story Processing Pipeline

A multi-stage sequential LLM pipeline built using **LangChain Expression Language (LCEL)** and **Google Gemini 3.6 Flash**. This project demonstrates chaining multiple task-specific prompts sequentially, where the output of one model call serves as the direct input for the next.

## Key Features

- **Sequential LCEL Chaining**: Utilizes LangChain pipe operators (`|`) to seamlessly link prompt templates, the chat model, and output parsers.
- **Multi-Stage Processing**:
  1. **Story Generation**: Creates a short 100-word narrative on a given topic.
  2. **Summarization**: Condenses the generated story into a single-sentence summary.
  3. **Translation**: Translates the single-sentence summary into Roman Urdu.
- **Output Parsing**: Integrates `StrOutputParser` across all chains to extract clean text strings from `AIMessage` objects.
- **Environment Security**: Uses `python-dotenv` to manage API keys securely.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: LangChain (`langchain-core`, `langchain-google-genai`)
- **LLM**: Google Gemini 3.6 Flash (`gemini-3.6-flash`)
- **Configuration**: `python-dotenv`

## Project Structure

```text
13_LangChain/
│
├── main.py          # Primary application script containing the sequential LCEL chains
├── .env             # Local environment file for API keys (Git ignored)
├── .gitignore       # Prevents sensitive files (.env, __pycache__) from being tracked
└── README.md        # Project documentation