age = input("Enter your age: ")
while not age.isdigit():
    print(f"Invalid age")
    age = input("Enter your age: ")

print(f"Valid age doubled is {age*2}")
