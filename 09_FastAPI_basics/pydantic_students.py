from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI application instance
app = FastAPI()


# Define Pydantic schema for Book validation
class Book(BaseModel):
    title: str
    author: str
    price: float
    pages: int
    genre: Optional[str] = None


# In-memory storage for books
books_db = []


# Endpoint to create a new book record
@app.post("/books")
def create_book(book: Book):
    books_db.append(book)
    return {
        "message": f"'{book.title}' added successfully!",
        "total_books": len(books_db),
    }


# Endpoint to retrieve all stored books
@app.get("/books")
def get_all_books():
    return {"books": books_db}


# Define Pydantic schema for Student validation
class Student(BaseModel):
    name: str
    age: int
    semester: int
    email: Optional[str] = None


# In-memory storage for students
students_db = []


# Endpoint to register a new student
@app.post("/students")
def add_student(student: Student):
    students_db.append(student)
    return {
        "Message": f"{student.name} added successfully",
        "total_students": len(students_db),
    }


# Endpoint to retrieve all registered students
@app.get("/students")
def view_all_students():
    return {"Students": students_db}