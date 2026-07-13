# CLI Calculator with Exception Handling

A professional, loop-driven Command Line Interface (CLI) calculator built with Python. This project focuses on input validation, custom error control, and preventing application crashes during execution.

## Core Features & Concepts

- **Exception Handling (`try-except-finally`):** Handles edge cases like `ZeroDivisionError` and invalid data types (`ValueError`) smoothly without crashing the script.
- **Custom Error Raising:** Explicitly raises a `ValueError` with a custom message if an unsupported mathematical operator is entered.
- **Continuous Execution Menu:** Utilizes a structured `while True` loop that keeps the utility running continuously until the user explicitly chooses to exit.
- **Data Sanitization:** Uses `.strip()` to clean user inputs from accidental trailing or leading spaces.

## How to Run

Navigate to this folder in your terminal and execute:
```bash
python calculator.py
