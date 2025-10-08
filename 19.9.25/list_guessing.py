import random
import os

list = []

lower = int(input("Enter your lower bound for the list: "))
upper = int(input("Enter your upper bound for the list: "))

while lower > upper:
    print("Lower cannot be higher than upper.")
    lower = int(input("Enter your lower bound for the list: "))
    upper = int(input("Enter your upper bound for the list: "))

for i in range(lower, upper+1):
    list.append(random.randint(lower,upper))

for i in range(len(list)):
    print(list[i], end=", ")
print()

print(f"> {random.choice(list)}")
