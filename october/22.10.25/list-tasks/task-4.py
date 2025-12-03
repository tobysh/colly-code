import random
nums = []
for i in range(15):
    nums.append(random.randint(1,25))
print(f"Largest: {max(nums)}\nSmallest: {min(nums)}")