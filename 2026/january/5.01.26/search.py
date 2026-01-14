import random

numbers = []

for i in range(15):
    numbers.append(random.randint(1,20))
numbers.sort()
while True:
    try:
        user_input = int(input("Enter a number to find\n>"))
        break
    except ValueError:
        print("Input must be a valid integer")

if sorted(numbers):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == user_input:
            print(f"Found {mid} at {numbers.index(mid)}")

        if numbers[mid] < user_input:
            left = mid + 1
        else:
            right = mid - 1
    print("Number not in list")
print(numbers)