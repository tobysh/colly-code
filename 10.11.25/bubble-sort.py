import random

def create_list():
    numbers = []
    for i in range(12):
        numbers.append(random.randint(-50,1000))
    return numbers

numbers = create_list()
print(numbers)
swapping = True
while swapping:
    swapping = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            swapping = True
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp
print(numbers)