email = input("Enter your email: ")
while "@" not in email or "." not in email or len(email) < 6:
    print("Invalid email format.")
    email = input("Enter your email: ")
email_parts = email.split("@")
username = email_parts[0]
domain_parts = email_parts[1].split(".")
print(email_parts)