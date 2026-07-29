# Student Management System (Python & SQLite3)

A lightweight, terminal-based CRUD application built with Python and SQLite3. This project demonstrates database connection handling, parameterized SQL queries, data validation, and basic error handling.

---

## Features

* **Create:** Add new students with auto-incrementing Primary Key IDs.
* **Read:** Fetch and display all registered students in a formatted layout.
* **Update:** Modify a student's semester using their unique Student ID.
* **Delete:** Remove student records with feedback using `cursor.rowcount`.
* **Data Validation:** Prevents empty names, numeric characters in names, and non-integer entries for IDs, age, and semester.
* **SQL Injection Safety:** Uses parameterized queries (`?` placeholders) for all database operations.

---

## Tech Stack

* **Language:** Python 3.x
* **Database:** SQLite3 (Built-in Python module)

---

## Project Structure

```text
├── student_management.py   # Main Python script with CLI logic
└── README.md              # Project documentation