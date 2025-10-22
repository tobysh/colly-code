count = int(input("How many numbers will you enter? "))
total = 0
i = 1
while i <= count:
    num = int(input("Enter number: "))
    total = total + num
    i = i + 1
average = total / count
print(f"Average is: {average}")
