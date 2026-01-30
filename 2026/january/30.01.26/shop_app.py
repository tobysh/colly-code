products = {"Bananas":3,
            "Chocolate":5,
            "Cereal":6
            } #key: {"product":stock}

def view_products():
    i=1
    for product in products.items():
        print(f"({i}) {product[0]}: {product[1]}")
        i += 1
        
def add_product():
    name = input("Enter the product name: ").capitalize()
    stock = None
    while not stock:
        temp_stock = input("Enter the current product stock: ")
        if temp_stock.isdigit():
            stock = int(temp_stock)
        else:
            print("Invalid stock")
    products.update({name: stock})
    print(f"Added {name} to products with stock {stock}")

def calculate_total_sales():
    price1 = None
    while not price1:
        temp_price1 = input("Enter the first price: ")
        try:
            price1 = float(temp_price1)
        except ValueError:
            print("Invalid Price")
            
    price2 = None
    while not price2:
        temp_price2 = input("Enter the first price: ")
        try:
            price2 = float(temp_price2)
        except ValueError:
            print("Invalid Price")
    total = round(price1+price2, 2)
    print(f"The total of {price1} and {price2} is {total}")

menu = """
--- Retail Shop Management ---
      (1) View products
       (2) Add product
   (3) Calculate total sales
------------------------------
"""

menu_dict = {
    1: view_products,
    2: add_product,
    3: calculate_total_sales
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