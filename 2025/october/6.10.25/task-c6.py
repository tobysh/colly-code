#Ask the user for three numbers and calculate the average, maximum, and minimum.
nums = []
for i in range(3):
    nums.append(int(input(f"({i+1}) Enter a number: ")))

print(f"""
Average: {sum(nums)/len(nums)}
Min: {min(nums)}
Max: {max(nums)}
      """)