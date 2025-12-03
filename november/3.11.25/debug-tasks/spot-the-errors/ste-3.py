email = input("Enter your email: ")
while "@" not in email or "." not in email:
    print("Invalid email format.")
    email = input("Enter your email: ")
print("Valid email entered.")