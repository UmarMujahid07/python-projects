# Library Management System (CLI)

A console-based Library Management System built in Python, using Object-Oriented Programming principles, JSON-based persistence, and structured error handling.

## Problem Statement

Build a menu-driven CLI application that allows a library to manage its book inventory — adding books, issuing/returning them to members, searching by title, and viewing all records — while ensuring data persists across program restarts and handles invalid input gracefully.

## Features

- **Add Book** — Add a new book with title, author, and ISBN (with duplicate ISBN prevention)
- **View All Books** — Display all books with their current status (Available/Issued)
- **Issue Book** — Issue a book by ISBN, with checks for existence and current status
- **Return Book** — Return a book by ISBN, validating it was actually issued
- **Search Book** — Case-insensitive partial search by title, returns all matches
- **Persistent Storage** — All data is saved to `library.json` and automatically reloaded on startup

## Concepts Applied

- **Object-Oriented Programming**
  - Two classes: `Book` (individual record) and `Library` (manager/container)
  - Composition (`Library` HAS-A list of `Book` objects) rather than inheritance
  - Encapsulated methods for all core operations (`add_book`, `issue_book`, `return_book`, `search_book`)
- **File Handling & JSON Persistence**
  - Custom `to_dict()` method to serialize `Book` objects into JSON-compatible dictionaries
  - Deserialization logic to reconstruct `Book` objects from saved JSON on load
- **Exception Handling**
  - Gracefully handles missing or corrupted data files (`FileNotFoundError`, `json.JSONDecodeError`)
- **Input Validation**
  - Empty-field checks for title, author, and search terms
  - ISBN format validation and whitespace sanitization (`.strip()`)
  - Duplicate ISBN prevention
- **Business Logic Validation**
  - Multi-level checks (e.g., a book can only be returned if it was actually issued)

## How to Run

```bash
python library.py
```

Follow the on-screen menu to add, view, issue, return, or search for books. Data is automatically saved to `library.json` after every change and reloaded the next time the program runs.