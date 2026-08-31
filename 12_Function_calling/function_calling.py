import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Tool Definitions with Type Hints and Explicit Docstrings

def get_weather(city: str) -> str:
    # Fetch current weather information for a specified city.
    fake_data = {
        "karachi": "32 Degree, Sunny",
        "lahore": "28 Degree, Cloudy",
        "islamabad": "25 Degree, Rainy"
    }
    return fake_data.get(city.lower(), "Weather data not available")


def calculate_tip(bill_amount: float, tip_percentage: float) -> float:
    # Calculate the total tip amount based on bill total and percentage.
    return bill_amount * (tip_percentage / 100)


def get_stock_price(company: str) -> str:
    # Retrieve the current stock price for a given company.
    fake_price = {
        "google": "$250",
        "tesla": "$500",
        "amazon": "$300"
    }
    return fake_price.get(company.lower(), "Stock price not available")


def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert currency from one denomination to another.
    Args:
        amount: Numerical amount of money to convert.
        from_currency: Base currency code (e.g., USD).
        to_currency: Target currency code (e.g., PKR).
    """
    # Fixed rate multiplier for demonstration
    converted_amount = amount * 280
    return f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}"

# Model Initialization & Automatic Tool Calling Setup

# Initializing Gemini Model with function tools attached
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[get_weather, calculate_tip, get_stock_price, convert_currency]
)

# Start multi-turn chat session with automatic function calling enabled
chat = model.start_chat(enable_automatic_function_calling=True)

# Execution Queries

# Query 1: Weather check (Triggers get_weather)
response1 = chat.send_message("What's the weather like in karachi?")
print("1. Weather Response:\n", response1.text)

# Query 2: Tip calculation (Triggers calculate_tip)
response2 = chat.send_message("What's a 15% tip on a $50 bill?")
print("2. Tip Response:\n", response2.text)

# Query 3: Stock lookup (Triggers get_stock_price)
response3 = chat.send_message("What's the stock price of Tesla?")
print("3. Stock Response:\n", response3.text)

# Query 4: Currency conversion (Triggers convert_currency)
response4 = chat.send_message("Convert 100 USD to PKR")
print("4. Currency Response:\n", response4.text)