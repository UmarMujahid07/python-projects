# Todo App API — Multi-User Backend with JWT Authentication

A complete, production-pattern backend combining routing, database persistence, and authentication into a single working system: a multi-user Todo API where each user can only access their own data.

## Problem Statement

Build a Todo API where multiple users can register, log in, and manage their own tasks — with strict data isolation, so no user can view or modify another user's todos, even though all data lives in the same database.

## What This Project Covers

- **User Registration** (`POST /register`) — creates a new user with a securely hashed password (passwords are never stored in plain text)
- **JWT Authentication** (`POST /login`) — validates credentials and issues a signed, time-limited access token, following the OAuth2 password flow (`OAuth2PasswordRequestForm`)
- **Protected Routes** — `get_current_user` dependency verifies the JWT on every protected request before the endpoint's logic runs
- **Multi-user data isolation**:
  - `POST /todos` — creates a new todo linked to the currently authenticated user via `owner_id`
  - `GET /todos` — returns *only* the todos belonging to the currently authenticated user
- **Relational data modeling** — `TodoDB.owner_id` is a foreign key referencing `UserDB.id`, enforcing the ownership relationship at the database level

## Architecture

```
10_Todo_App_API/
├── database.py   # SQLAlchemy engine, session factory, and get_db dependency
├── models.py     # UserDB and TodoDB tables (linked via ForeignKey)
├── auth.py       # Password hashing (bcrypt), JWT creation/verification, get_current_user
└── main.py       # FastAPI app and all route definitions
```

## Key Concepts Covered

- **Separation of concerns** — Pydantic models (`UserCreate`, `TodoCreate`) validate incoming request data, while SQLAlchemy models (`UserDB`, `TodoDB`) define database structure — kept as distinct classes with distinct responsibilities
- **Password security** — one-way hashing with `bcrypt`; plain-text passwords are never stored or returned in API responses
- **JWT lifecycle** — token creation with an expiry claim, and token verification via dependency injection on every protected route
- **Dependency injection** — `Depends(get_db)` and `Depends(get_current_user)` used together to give each request both a database session and a verified identity
- **Foreign key relationships** — linking rows across tables (`todos.owner_id → users.id`) to model real-world ownership

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (SQLite)
- Pydantic
- passlib (bcrypt)
- python-jose (JWT)

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy passlib python-jose bcrypt
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the full flow:
1. `POST /register` — create a user
2. `POST /login` (or the "Authorize" button) — get an access token
3. `POST /todos` — create a todo (requires authentication)
4. `GET /todos` — view only your own todos

## What I Learned

Building this reinforced a recurring pattern in authenticated APIs: the verified identity from a token (`current_user`) is just a username string — it has to be used to look up the *actual* database record before any ownership-based fields (like `owner_id`) can be set or filtered on. Conflating the two (treating a username string as if it were a database object) was a repeated bug during development, and fixing it cemented the distinction between "who the request claims to be" and "the actual database record for that user."
