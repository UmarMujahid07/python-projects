# LLM Chatbot (Gemini API)

A command-line chatbot built using Google's Gemini API — the first hands-on step into working with Large Language Models programmatically.

## What This Project Covers

- **API Authentication** — securely loading an API key from a `.env` file using `python-dotenv`, keeping secrets out of version control
- **Making LLM API calls** — using the `google-generativeai` SDK to send prompts and receive generated responses
- **Interactive CLI loop** — a `while True` menu-style loop (same pattern used in earlier CLI projects) that takes user input and exits on command
- **Error handling** — wrapping API calls in `try/except` to handle issues like invalid keys or network failures gracefully

## A Known Limitation (by design)

This version of the chatbot does **not** retain conversation history — each message is sent to the model independently, with no memory of previous exchanges. For example, telling the bot your name in one message and asking for it in the next will not work, because the model has no context window carrying prior messages forward.

This is intentional groundwork for the next step: adding conversation memory, so the model can maintain context across a multi-turn conversation.

## Tech Stack

- Python
- Google Generative AI SDK (`google-generativeai`)
- python-dotenv

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
