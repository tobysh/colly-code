#Create a program that checks if a number is between 10 and 20 and is even.

num =int(input("Enter a number: "))
if num >= 10 and num <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is not between 10 and 20")

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")