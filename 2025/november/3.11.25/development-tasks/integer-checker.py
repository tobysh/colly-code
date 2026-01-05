"""
Write a program that.
1. Asks the user for a number.
2. Check if it is an integer.
3. If valid, convert it to int and print the square.
4. Otherwise, print “Invalid input”.
"""

num_string = input("Enter a number: ")
if num_string.isdigit():
    print(int(num_string)**2)
else:
    print("Invalid input")