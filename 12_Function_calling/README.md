# Function Calling with LLMs (Gemini API)

An exploration of function/tool calling — giving an LLM the ability to recognize when it needs external data or computation, and automatically call the right Python function to get it.

## What This Project Covers

- **Defining callable tools** — writing plain Python functions with clear type hints (`city: str`, `amount: float`), which the Gemini SDK reads to understand what each function does and what arguments it needs
- **Registering tools with the model** — passing functions directly via the `tools=[...]` parameter
- **Automatic function calling** — using `enable_automatic_function_calling=True` so the SDK detects when the model wants to call a function, executes it, and feeds the result back to the model automatically
- **Multi-tool decision-making** — giving the model more than one tool (`get_stock_price`, `convert_currency`, `get_weather`, `calculate_tip`) and observing it correctly choose the right tool based on the user's question

## Example Interactions

| User Question | Tool Called | Result |
|---|---|---|
| "What's the weather in Karachi?" | `get_weather("Karachi")` | 32°C, Sunny |
| "What's a 15% tip on a $50 bill?" | `calculate_tip(50, 15)` | $7.50 (plus model-computed total: $57.50) |
| "What's the stock price of Tesla?" | `get_stock_price("Tesla")` | $500.00 |
| "Convert 100 USD to PKR" | `convert_currency(100, "USD", "PKR")` | 28,000 PKR |

## Why This Matters

This is the foundational pattern behind AI "agents" — rather than just generating text, the model can decide *when* it lacks information and *which* real function to call to get it, then reason over the result to produce a final answer. This is a direct stepping stone toward building LangChain/LangGraph agents.

## Tech Stack

- Python
- Google Generative AI SDK (`google-generativeai`)
- python-dotenv

## How to Run

```bash
pip install google-generativeai python-dotenv
```

Set up a `.env` file with your API key, then run the script and try asking questions that require different tools.
