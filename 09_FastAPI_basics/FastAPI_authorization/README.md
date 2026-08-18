# FastAPI Authentication (JWT)

An introduction to securing FastAPI endpoints — covering password hashing, JWT token generation, and a working login flow.

## What's Inside

### `auth.py`
Core authentication utilities, kept separate from the API routes:

- **Password hashing** — `hash_password()` and `verify_password()`, using `passlib`'s `bcrypt` scheme. Passwords are never stored or compared in plain text.
- **JWT token generation** — `create_access_token()`, which builds a signed, time-limited token (30-minute expiry) using `python-jose`.

### `main.py`
- A `POST /login` endpoint that:
  1. Looks up the user in a simulated user database
  2. Verifies the submitted password against the stored hash
  3. Returns an `HTTPException` (401) on invalid credentials
  4. On success, issues a signed JWT access token

## Key Concepts Covered

- **Authentication vs. Authorization** — verifying *who* a user is, vs. what they're allowed to do
- **One-way password hashing** — why passwords are hashed rather than encrypted or stored as-is, and how `verify()` checks a password without ever "reversing" a hash
- **JWT structure** — payload (`sub` claim for user identity), expiry (`exp` claim), and signing with a secret key to prevent tampering
- **Separation of concerns** — keeping authentication logic (`auth.py`) separate from route definitions (`main.py`), following the same pattern used for database logic in earlier FastAPI work

## Tech Stack

- Python
- FastAPI
- passlib (bcrypt)
- python-jose (JWT)

## How to Run

```bash
pip install fastapi uvicorn passlib python-jose bcrypt
uvicorn main:app --reload
```

Test via `http://127.0.0.1:8000/docs` — POST to `/login` with a valid username/password to receive an access token. Note: login endpoints must be tested through `/docs` (or a tool like `requests`), not by visiting the URL directly in a browser, since browsers send GET requests by default.

## Note on the Secret Key

The `SECRET_KEY` in `auth.py` is hardcoded for learning purposes. In a production application, this should be loaded from an environment variable and never committed to version control.
