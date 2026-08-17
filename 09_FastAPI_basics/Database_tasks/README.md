# Task Management API (Database Integration)

A FastAPI application that integrates SQLite and SQLAlchemy ORM to manage task records dynamically with persistent database storage.

---

## Features

* **SQLite Integration:** Uses SQLAlchemy ORM to manage database tables and connections.
* **Request Validation:** Employs Pydantic schemas for data parsing and type safety.
* **REST API Endpoints:** Supports task creation and filtering (all tasks vs. pending tasks).
* **Interactive Docs:** Built-in Swagger UI documentation generated automatically.

---

## Project Structure

```text
03_database_tasks/
├── database.py   # Database connection setup & session yield dependency
├── models.py     # SQLAlchemy ORM model (tasks table schema)
└── main.py       # FastAPI instance, Pydantic schema, & API route definitions