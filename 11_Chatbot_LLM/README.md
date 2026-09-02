# LLM Chatbot (Gemini API)

A command-line chatbot built using Google's Gemini API — featuring multi-turn conversation memory using stateful chat sessions.

## What This Project Covers

- **API Authentication** — securely loading an API key from a `.env` file using `python-dotenv`, keeping secrets out of version control
- **Stateful Multi-Turn Chat** — using `model.start_chat(history=[])` and `chat.send_message()` to persist conversation memory across turns
- **Interactive CLI Loop** — a continuous terminal interface loop that takes user input and exits on command
- **Error Handling** — wrapping API calls in `try/except` blocks to handle network or API issues gracefully

## Conversation Context Memory

Unlike single-shot prompt generation, this chatbot maintains continuous context memory across user turns. Telling the bot your name in one turn allows it to accurately remember and reference your name in subsequent questions within the same session.

## Tech Stack

- **Python**: 3.x
- **SDK**: Google Generative AI (`google-generativeai`)
- **LLM**: Google Gemini 3.6 Flash (`gemini-3.6-flash`)
- **Configuration**: `python-dotenv`


## How to Run

```bash
pip install google-generativeai python-dotenv
```

Create a `.env` file in this folder with your API key:
```
GOOGLE_API_KEY=your-key-here
```

Then run:
```bash
python chatbot.py
```

Type your messages, and type `exit` to quit.

## Security Note

The `.env` file is excluded from version control via `.gitignore`. Never commit API keys directly into source code or push them to a public repository.
