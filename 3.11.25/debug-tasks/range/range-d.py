quantity = int(input("Enter quantity (1-50): "))
while quantity < 1 or quantity > 50:
    print("Invalid quantity!")
    quantity = int(input("Enter quantity (1-50): "))
print("Quantity accepted:", quantity)
