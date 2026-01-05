num = input("Enter a number: ")
while not num.isdigit():
    print("Invalid input!")
    num = input("Enter a number: ")
print("Number accepted:", num)