import re
import string
import os

USER_FILE = "/workspaces/colly-code/3.11.25/development-tasks/users.json"

def get_users():
    if os.path.isfile(USER_FILE):
        with open(USER_FILE, "r") as file:
            key = file.read()
    else:
        with open(USER_FILE, "w") as file:
            file.write(key)

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
    name = input("Name: ").strip().capitalize()
    while name == "":
        print("Name cannot be empty.")
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
    
user_name = name()
user_age = age()
user_email = email()
user_password = password()

user = create_user(user_name, user_age, user_email, user_password)
print_user(user)