import random

def get_list(quant):
    good_list = False
    while not good_list:
        numbers = []
        for i in range(quant):
            numbers.append(random.randint(1,50))
        for number in numbers:
            print(number, end=", ")
        print()
        user_op = input("(Y/N) Is this a good list?\n").lower()
        good_list = not user_op == "n"
    return numbers
while True:   
    quant = input("How many numbers do you want to generate?\n>")
    if quant.isdigit():
        numbers = get_list(int(quant))
        break
    else:
        print("Enter a positive integer")

peaks = []
for i in range(len(numbers)):
    length = len(numbers)-1
    while i != length:
        if i == 0:
            if numbers[i] > numbers[i+1]:
                peaks.append(i)
        else:
            if numbers[i] > numbers[i+1] and numbers[i] > numbers[i-1]:
                peaks.append(i)
        print(i)
                
for peak in peaks:
    print(numbers[peak], end=", ")