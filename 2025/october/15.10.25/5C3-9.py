correct = "letmein"
password = input("Enter password: ")
while password != correct:
    print("Access denied")
    password = input("Enter password: ")
print("Access granted")
