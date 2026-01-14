age = int(input("Enter your age (18-65): "))
while age < 18 or age > 65:
    print("Age must be between 18 and 65.")
    age = int(input("Enter your age (18-65): "))
print("Valid age entered.")