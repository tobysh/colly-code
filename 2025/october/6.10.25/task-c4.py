#Ask the user for their age and check if they are eligible to vote (age ≥ 18).

age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
else:
    print("You're too young to vote")