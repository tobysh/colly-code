numbers = [13,10,13,2,8,12]

def get_number():
    try:
        target = int(input("Enter your target\n>"))
        return target
    except ValueError:
        print("This is not a whole number.")
    return get_number()

found = False
target = get_number()
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Found {target} at position {i+1}")
        found = True
if not found:
    print(f"Could not find {target}")