age = int(input("Enter your age: "))

if age < 12:
    price = 6
elif 12 <= age <= 17:
    price = 8
else:
    price = 10

print(f"Ticket price: £{price}")