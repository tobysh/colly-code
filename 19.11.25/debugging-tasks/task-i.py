def add(a, b):
    print(a + b)
def greet(name):
    return f"Hello, {name}" 
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
result = add(num1, num2)
print(f"Hello there {greet(input("Your name"))}, {num1} + {num2} = result")