prices = {
    "small": 5.00,
    "medium": 8.00,
    "large": 10
}

selection = prices.get(input("What size pizza do you want? (small/medium/large)\n>").lower().strip())

if selection == None:
    print("Invalid choice")
else:
    extra_cheese = (input("Would you like extra cheese? (Yes/No)\n>").lower().strip() == "yes")
    if extra_cheese: selection += 0.50
    print(f"The pizza will be {selection:.2f}")
    
    