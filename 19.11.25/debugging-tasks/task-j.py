def multiply(x, y):
    return x * y

nums = [2, 4, 6]
for i in range(len(nums)):
    for j in range(len(nums)):
        print(multiply(nums[i], nums[j]))

data = {"names": ["Alice", "Bob"], "ages": [20, 21]}
for i in range(len(data)):
    print(data["names"][i], data["ages"][i])