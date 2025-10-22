num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

try:
    answer=num1/num2
    print(answer)
except ZeroDivisionError:
    print("Cannot divide by 0")