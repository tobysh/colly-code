import re
import string
import os
import json

USER_FILE = "/workspaces/colly-code/3.11.25/development-tasks/users.json"

def register(users: list):
    user = create_user(name(), age(), email(), password())
    user.update({"id": len(users)+1})
    users.append(user)
    save_users(users)
    print_user(user)

def login(users: list):
    attempted_user = None
    name = input("Enter your name: ")
    for user in users:
        if user.get("name") == name:
            attempted_user = user
    if attempted_user == None:
        print("No user found")
    else:
        password = input("Enter your password: ")
        if password == attempted_user["password"]:
            print(f"Welcome, {name}")

def get_users():
    if os.path.isfile(USER_FILE):
        with open(USER_FILE, "r") as file:
            user_json = file.read()
            users = json.loads(user_json)
            return users
    else:
        with open(USER_FILE, "w") as file:
            file.write("[]")
            return []

def save_users(users: dict):
    user_json = json.dumps(users)
    with open(USER_FILE, "w") as file:
            file.write(user_json)
            print("Saved users to users.json")

def create_user(name: str, age: int, email: str, password: str):
    user = {
        "name":name,
        "age": age,
        "email": email,
        "password": password
    }
    return user

def print_user(user: dict):
    printable_password = ""
    for i in range(len(user["password"])):
        printable_password += "*"
    print(f"""
Name: {user["name"]},
Age: {user["age"]},
Email: {user["email"]},
Password: {printable_password}
          """)

def name():
    users = get_users()
    name = input("Name: ").strip().capitalize()
    while name == "":
        print("Name cannot be empty.")
        name = input("Name: ").strip()
    while True:
        for user in users:
            if user.get("name") == name:
                print("Name is in use.")
            name = input("Name: ").strip()
    return name

def age():
    age = input("Age: ").strip()
    while not age.isdigit():
        print("Age must be a number.")
    while int(age) > 120 or int(age) < 0:
        print("Age must be between 0 and 120")
    return int(age)


def email():
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        user_email = input("Email: ").strip()
        if user_email == "":
            print("Email cannot be empty.")
        elif not re.match(pattern, user_email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            return user_email

def password():
    while True:
        password = input("Password: ").strip()
        while password == "":
            print("Password cannot be empty.")
            password = input("Password: ").strip()
        while len(password) < 8 or len(password) > 32:
            print("Password must be between 8 and 32 characters.")
            password = input("Password: ").strip()
        while not any(char in string.punctuation for char in password):
            print("Password must contain punctuation.")
            password = input("Password: ").strip()
        while password.lower() == password:
            print("Password must contain at least one upper-case letter.")
            password = input("Password: ").strip()
        confirm_password = input("Confirm password: ").strip()
        if password == confirm_password:
            return password
        else:
            print("Passwords must match")

def menu():
    menu_text = """
=== Login or Register ===

(1): Login
(2): Register

=========================
"""
    print(menu_text)
    choice = input(">")
    choice_map = {
        "1": login,
        "2": register
    }
    return(choice_map[choice])

users = get_users()
if len(users) == 0:
    print("No users stored, redirecting to registration...")
    register(users)

menu()(users)