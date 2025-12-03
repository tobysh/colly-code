num = input("Enter a number: ")
while num.isdigit() == False:
    num = input("Enter a number: ")
    print("Invalid input!")
print("Number accepted:", num)
