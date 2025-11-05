username = input("Enter a username: ").strip()
while username == "":
    print("Username is invalid")
    username = input("Enter a username: ").strip()
password = input("Enter a password: ")
length = len(password)
while length < 6 or length > 12:
    print("Password must be between 6 and 12 characters.")
    password = input("Enter a password: ")
    length = len(password)

print(f"Hello, {username}.")