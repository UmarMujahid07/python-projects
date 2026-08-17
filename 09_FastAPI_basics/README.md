# FastAPI Basics

An introduction to building web APIs with FastAPI — covering routing, request validation with Pydantic, and database integration with SQLAlchemy.

---

## What's Inside

### 1. `main.py`
A foundational 5-endpoint API demonstrating core FastAPI routing concepts:
- **`GET /`** — Root endpoint returning a basic welcome message.
- **`GET /books/{book_id}`** — Path parameter example retrieving dynamic values directly from the URL path.
- **`GET /search`** — Query parameter example supporting optional filtering.
- **`GET /greet/{name}`** — Path parameter example generating personalized responses.
- **`GET /add`** — Query parameter example performing addition on required integer inputs.

### 2. `pydantic_students.py`
Demonstrates structured data modeling and payload validation using Pydantic `BaseModel`:
- **`POST /books` & `GET /books`** — Endpoints for creating and fetching book records.
- **`POST /students` & `GET /students`** — Endpoints for validating student details (including optional fields like `email`).

### 3. `Database_tasks/`
A full task management module integrating persistent SQLite database storage via SQLAlchemy ORM:
- **`database.py`** — Handles database engine creation, session generation, and request dependency injection (`get_db`).
- **`models.py`** — Defines the `TaskDB` database schema/table mapping.
- **`main.py`** — Exposes REST API routes (`POST /tasks`, `GET /tasks`, `GET /tasks/pending`) backed by SQLite storage.

---

## Key Concepts Covered

- **Decorators (`@app.get`, `@app.post`)** — Binding HTTP verbs and URL paths to backend handler functions.
- **Path & Query Parameters** — Parsing embedded path segments and URL search queries with type coercion.
- **Pydantic Schemas** — Automatic request body validation and structured JSON serialization.
- **SQLAlchemy ORM** — Mapping Python models to SQLite database tables and managing database sessions.
- **Interactive Documentation** — Swagger UI automatically generated at `/docs`.

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn (ASGI Server)

---

## How to Run

### Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy
### Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy
