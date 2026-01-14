def calculate_basket_total(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += round((prices[i] * quantities[i]), 2)
    vat = total * 0.2
    final_total = total + vat
    return final_total
prices = []
quantities = []
for i in range(3):
    try:
        prices.append(float(input(f"({i+1}) Enter the item of a price: ")))
    except ValueError:
        print("Enter a valid number.")
    try:
        quantities.append(int(input(f"({i+1}) Enter the quantity for the item: ")))    
    except ValueError:
        print("Enter a valid integer.")
print(calculate_basket_total(prices, quantities))
