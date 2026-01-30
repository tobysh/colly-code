food_menu = {
    "fish \'n chips": 7.49,
    "sausage and mash": 6.50,
    "beef burger": 5.99
}
order = {
    
}
def view_menu():
    i=1
    for product in food_menu.items():
        print(f"({i}) {product[0]}: {product[1]}")
        i += 1
        
def take_order():
    while True:
        query = input("What would you like to eat? (Enter -1 when you\'re all done)\n>").lower()
        if query == "-1":
            break
        elif not food_menu.get(query):
            print("Sorry, that item doesn\'t exist.")
        else:
            while True:
                quantity = None
                while not quantity:
                    try:
                        quantity = int(input("How many would you like?\n>"))
                    except ValueError:
                        print("Invalid quantity")
                break
            print(f"Added {quantity} of {query} to your order!")
            order.update({query: quantity})
    print("All set!")
    
def calculate_bill():
    subtotal = 0
    for item in order.items():
        subtotal += food_menu.get(item[0]) * item[1]
    print(f"Your bill is {subtotal}")
        
            
            
        
    
        
                    
        

menu = """
--- Resturant Ordering System ---
    (1) View menu
    (2) Take order
    (3) Calculate Bill
    (4) Exit
------------------------------
"""

menu_dict = {
    1: view_menu,
    2: take_order,
    3: calculate_bill,
    4: exit
}

while True:
    print(menu)

    choice = None
    while not choice:
        try:
            choice = int(input(">"))
        except ValueError:
            print("Invalid choice")
    menu_dict[choice]()