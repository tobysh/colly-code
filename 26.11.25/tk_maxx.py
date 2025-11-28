

STORE_NAME="TK Maxx"
print(f"Welcome to the {STORE_NAME} storage system!")
products=[
    {"name":"Laptop",
    "price":1200,
    "stock":10
    }
]

for i in range(1001, 1011):
    print(i)

while True:
    price = input("Enter a product price:\n")
    try:
        price = int(price)
        if price == -1:
            break
    except ValueError:
        print("Enter a valid number")

print(f"{products[0]["name"]} stock: {products[0]["stock"]}")
inventory=[["Name","Price","Stock"],["Laptop",1200,10],["Mouse", 25, 50],["Keyboard",45,30]]
print(inventory[2][1])

def apply_discount(price:int=100):
    discounts={
        "100":0,
        "101":10,
        "201":20,
        "501":25
    }
    for discount in (discounts):
        if price >= int(discount):
            reduction = discounts[discount]
    print(f"You get a {reduction}% discount")

price = -1
while price == -1:
    buffer = input("Enter a price: \n")
    if buffer.isdigit():
        price = int(buffer)

apply_discount(price)