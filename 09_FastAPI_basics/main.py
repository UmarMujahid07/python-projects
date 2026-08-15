from fastapi import FastAPI

app = FastAPI()

# Root endpoint : basic welcome message, no parameters needed
@app.get("/")
def greet():
    return {"message": "Welcome to my API"}


# Path Parameter example : {book_id} is REQUIRED, comes directly from the URL
# e.g. /books/5 -> book_id = 5
@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id, "title": "Sample book"}


# Query Parameter example : OPTIONAL filters, passed after "?" in the URL
# e.g. /search?title=Harry&author=Rowling
@app.get("/search")
def search_books(title: str = None, author: str = None):
    return {"searching_title": title, "searching_author": author}


# Path Parameter example : greets whoever's name is given in the URL
# e.g. /greet/Umar -> name = "Umar"
@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello, {name}!"}


# Query Parameter example : both values are REQUIRED here (no default given)
# e.g. /add?a=5&b=3
@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}