import random
nums = []
for i in range(15):
    nums.append(random.randint(1,10))
tracked = int(input("Enter a number (1-10) to query occurances: "))
print(f"{tracked} appears {nums.count(tracked)} times in the list")