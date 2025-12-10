

# College Library Management System (Procedural Version)
# Approximately 200 lines of Python code

import datetime

books = {}
students = {}
transactions = []

# ----------------------------
# Book Management Functions
# ----------------------------

def add_book(book_id, title, author, copies):
    if book_id in books:
        print("Book ID already exists!")
        return
    if book_id == 0 or copies == 0:
        print("Book ID or copies cannot be zero.")
        return
    
    else:
        if book_id.isdigit():
            books[book_id] = {
                "title": title,
                "author": author,
                "copies": copies
            }
            print(f"Book '{title}' added successfully.") 
        else:
            print("Book ID and Copies must both be integers above -1")

def view_books():
    if not books:
        print("No books in the library.")
        return
    print("\n--- Book List ---") 
    for bid, info in books.items():
        print(f"{bid}: {info['title']} by {info['author']} (Copies: {info['copies']})")

# ----------------------------
# Student Management Functions
# ----------------------------

def view_students():
    if not students:
        print("No students registered.")
        return
    print("\n--- Student List ---")
    for sid, info in students.items():
        print(f"{sid}: {info['name']} (Borrowed: {len(info['borrowed'])})")

def add_student(student_id, name):
   
    if not student_id.isdigit():
        print("Invalid student ID.") 
        return

    if student_id in students:
        print("Student ID already exists!")
        return
    students[student_id] = {
        "name": name,
        "borrowed": []
    }
    print(f"Student '{name}' added successfully.")

# ----------------------------
# Borrowing and Returning
# ----------------------------

def borrow_book(student_id, book_id):
    if student_id not in students:
        print("Student not found.")
        return
    if book_id not in books:
        print("Book not found.")
        return

    if books[book_id]["copies"] == 0:
        print("No copies available.")
        return

    students[student_id]["borrowed"].append(book_id)
    books[book_id]["copies"] -= 1 

    transaction = {
        "student_id": student_id,
        "book_id": book_id,
        "action": "borrow",
        "date": datetime.date.today()
    }
    transactions.append(transaction)

    print(f"Book '{books[book_id]['title']}' borrowed by {students[student_id]['name']}.")

def return_book(student_id, book_id):
    if student_id not in students:
        print("Student not found.")
        return
    if book_id not in books:
        print("Book not found.")
        return

    if book_id not in students[student_id]["borrowed"]:
        print("Student did not borrow this book.")
        return

    students[student_id]["borrowed"].remove(book_id)
    books[book_id]["copies"] += 1  # LOGICAL-1: Should add back a copy, not subtract

    transaction = {
        "student_id": student_id,
        "book_id": book_id,
        "action": "return",
        "date": datetime.date.today()
    }
    transactions.append(transaction)

    print(f"Book '{books[book_id]['title']}' returned by {students[student_id]['name']}.")

# ----------------------------
# Reporting
# ----------------------------

def view_transactions():
    if not transactions:
        print("No transactions recorded.")
        return
    print("\n--- Transactions ---")
    for t in transactions:
        action = "Returned" if t["action"] == "borrow" else "Borrowed"
        print(f"{t['date']} - {action}: {books[t['book_id']]['title']} by {students[t['student_id']]['name']}")

# ----------------------------
# Menu System
# ----------------------------

def menu():
    while True:
        print("\n===== COLLEGE LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Student")
        print("4. View Students")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View Transactions")
        print("8. Exit")

        choice = input("Enter option: ")

        if choice == "1": 
            bid = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            add_book(bid, title, author, copies)
        elif choice == "2":
            view_books()
        elif choice == "3":
            sid = input("Student ID: ")
            name = input("Student Name: ")
            add_student(sid, name)
        elif choice == "4":
            view_students()
        elif choice == "5":
            sid = input("Student ID: ")
            bid = input("Book ID: ")
            borrow_book(sid, bid)
        elif choice == "6":
            sid = input("Student ID: ")
            bid = input("Book ID: ")
            return_book(sid, bid) 
        elif choice == "7":
            view_transactions()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()