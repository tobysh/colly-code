import random as r

magic_number = r.randint(1,10)

while int(input("Choose a number from 1-10: ")) != magic_number:
    print("Wrong!")
print("Correct!")