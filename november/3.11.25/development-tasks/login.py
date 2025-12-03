username_prompt = "Enter a username: "
password_prompt = "Enter a password: "
username = input(username_prompt).strip()
while username == "":
    print("Username cannot be empty.")
    username = input(username_prompt).strip()
password = input(password_prompt).strip()
while len(password) < 6:
    print("Password is too short.")
    password = input(password_prompt).strip()
while len(password) > 12:
    print("Password is too long.")
    password = input(password_prompt).strip()

print("Login successful.")