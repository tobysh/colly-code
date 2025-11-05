prompt = "Enter a password (8-12 characters): "
password = input(prompt).strip()
while len(password) < 8:
    print("Password is too short.")
    password = input(prompt).strip()
while len(password) > 12:
    print("Password is too long.")
    password = input(prompt).strip()
