# FastAPI Basics

An introduction to building web APIs with FastAPI — covering routing, path parameters, query parameters, and automatic interactive documentation.

## What's Inside

### `main.py`
A simple 5-endpoint API demonstrating core FastAPI concepts:

- **`GET /`** — a basic root endpoint returning a welcome message
- **`GET /books/{book_id}`** — path parameter example; `book_id` is required and comes directly from the URL (e.g. `/books/5`)
- **`GET /search`** — query parameter example with optional filters (e.g. `/search?title=Harry&author=Rowling`)
- **`GET /greet/{name}`** — path parameter example that returns a personalized greeting
- **`GET /add`** — query parameter example with two required integer inputs (e.g. `/add?a=5&b=3`)

## Key Concepts Covered

- **Decorators** (`@app.get(...)`) — registering a function as a handler for a specific route and HTTP method
- **Path parameters** — required values embedded directly in the URL (`{book_id}`, `{name}`)
- **Query parameters** — optional or required values passed after `?` in the URL
- **Type hints** — FastAPI automatically validates incoming data (e.g. rejecting non-integer input to `book_id`)
- **Automatic documentation** — FastAPI generates an interactive API explorer at `/docs`, with no extra setup required

## Tech Stack

- Python
- FastAPI
- Uvicorn (ASGI server)

## How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then visit `http://127.0.0.1:8000/docs` to explore and test each endpoint interactively.