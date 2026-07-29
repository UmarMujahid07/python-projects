import sqlite3
# if not exists, python will create a database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        semester INTEGER
    )
""")
connection.commit()

def add_student(name, age, semester):
    cursor.execute("INSERT INTO students (name,age,semester) VALUES (?,?,?)", (name,age,semester))
    connection.commit()
    print(f"{name} added successfully..!")
    
def view_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No students found!")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Semester: {row[3]}")
    
def update_semester(new_semester, student_id):
        cursor.execute("UPDATE students SET semester = ? WHERE id = ?", (new_semester, student_id))
        connection.commit() 
        if cursor.rowcount == 0:
            print(f"No student found with id: {student_id}")
        else:
            print("Semester updated successfully.!")
        
        
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id, ))
    connection.commit()
    if cursor.rowcount == 0:
        print(f"No student to delete with ID: {student_id}")
    else:
        print(f"Student with ID {student_id} deleted successfully.!")
    

while True:
    print("\n1. Add Student\n2. View All Students\n3. Update Semester\n4. Delete Student\n5. Exit")
    choice = input("Enter an option: ")
    
    if choice == "1":
        name = input("Enter student's name: ")
        while name.strip() == "" or any(char.isdigit() for char in name):
            print("Name cannot be empty or contain numbers!")
            name = input("Enter student's name: ")
        while True:
            try:
                age = int(input("Enter student's age: "))
                break
            except ValueError:
                print("Invalid age..!")
        while True:
            try:
                semester = int(input("Enter semester: "))
                break
            except ValueError:
                print("Invalid semester..!")
            
        add_student(name,age,semester)
    elif choice== "2":
        view_all_students()
    elif choice == "3":
        while True:
            try:
                student_id= int(input("Enter student id: "))
                break
            except ValueError:
                print("Invalid id!")
        while True:
            try:
                new_semester = int(input("Enter new semester: "))
                break
            except ValueError:
                print("Invalid semester!")
        update_semester(new_semester, student_id)
    elif choice == "4":
        while True:
            try:
                student_id = int(input("Enter student's id to delete: "))
                break
            except ValueError:
                print("Enter valid id!")
            delete_student(student_id)
    elif choice == "5":
        connection.close()
        print("Existing the system..!")
        break
    else:
        print("Invalid choice..!")