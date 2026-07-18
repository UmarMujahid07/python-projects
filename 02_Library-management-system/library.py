import json
class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False
        
    def to_dict(self):
        # converting book object into dictionary
        return {
            "title" : self.title,
            "author" : self.author,
            "isbn" : self.isbn,
            "is_issued" : self.is_issued
        }
        
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("Book already exist")
                return
        new_book = Book(title,author,isbn)
        self.books.append(new_book)
        print(f"{title} added successfully")
    def show_all_books(self):
        if not self.books:
            print("No book in library yet!")
        for index, book in enumerate(self.books):
            status = "Issued" if book.is_issued else "Available"
            print(f"Book {index+1}:\nTitle: {book.title}\tAuthor: {book.author}\tStatus: {status}")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_issued:
                    print("Book already issued!")
                else:
                    book.is_issued = True
                    print("Book issued successfully")
                return
        print("Book not found!")
        
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully!")
                else:
                    print("This book was not issued, cannot return")
                return
        print("ISBN does not exist..!")  
        
    def search_book(self,title):
        if title.strip() == "":
            print("Please enter a search term: ")
            return    
        
        found = False
        print("\nAvailable books: ")
        for book in self.books:
            if title.lower() in book.title.lower():
                found= True
                status = "Issued" if book.is_issued else "Available"
                print(f"\nTitle: {book.title}\tAuthor: {book.author}\tStatus: {status}",end="")
        if not found:
            print("Title does not match..! ")
        
    def save_to_file(self):
        with open("library.json", "w") as file:
            books_as_dicts = [book.to_dict() for book in self.books]
            json.dump(books_as_dicts, file, indent =4)
    
    def load_from_file(self):
        try:
            with open("library.json", "r") as file:
                books_as_dicts = json.load(file)
                for b in books_as_dicts:
                    new_book = Book(b["title"], b["author"], b["isbn"])
                    new_book.is_issued = b["is_issued"]
                    self.books.append(new_book)
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            self.books = []
            
library = Library()
library.load_from_file()

while True:

    print("\n\n1. Add Book\n2. Show All Books\n3. Issue Book\n4. Return Book\n5. Search Book\n6. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        title = input("Enter title: ")
        while title.strip() == "":
            print("Title can not be empty!")
            title= input("enter title: ")
        author = input("Enter author's name: ")
        while author.strip() == "":
            print("Author's name can not be empty!")
            author = input("Enter author's name: ")
        isbn = input("Enter ISBN: ").strip()
        while not isbn.replace("-", "").isdigit():
            print("Invalid ISBN format!")
            isbn = input("Enter ISBN: ").strip()
        library.add_book(title,author,isbn)
        library.save_to_file()
    
    elif choice == "2":
        print("Showing all books:\n")
        library.show_all_books()
    
    elif choice=="3":
        search_isbn = input("Enter ISBN to issue: ").strip()
        library.issue_book(search_isbn)
        library.save_to_file()
        
    elif choice=="4":
        return_isbn = input("Enter ISBN: ").strip()
        library.return_book(return_isbn)
        library.save_to_file()
        
    elif choice=="5":
            search_title = input("Enter title to search: ")
            library.search_book(search_title)
    
    elif choice == "6":
        print("Thank you for using the system!")
        break
    
    else:
        print("Invalid choice..!")