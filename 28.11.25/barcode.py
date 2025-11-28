import math
barcode = ""
while not barcode.isdigit() or not len(barcode)==13:
    barcode = input("Enter your barcode: ").strip()
barcode = list(barcode)
check_digit = barcode.pop()
for i in range(len(barcode)):
    barcode[i] = int(barcode[i])
    if i%2==1:
        if i != 13:
            barcode[i] *= 3
bar_sum = sum(barcode)        
sub = math.ceil(bar_sum) - bar_sum
if sub == check_digit:
    print("Valid barcode")