shopping_lists={}
customer_details={
    "Alice":250,
    "Bob":120,
    "Charlie":600
}

def get_number(prompt:str="Enter a positive number: ", posOnly:bool=True):
    if posOnly:
        while True:
            num = input(prompt)
            if prompt.isdigit():
                num = int(num)
                return num
            else:
                print("Invalid number.")
    else:
        while True:
            num = input(prompt)
            try:
                num = int(num)
                return num
            except ValueError:
                print("Not a number.")

def add_to_list():
    customer_name=input("Enter your name: ").capitalize()
    items=[]
    for i in range(3):
        items.append(input(f"Enter item {i+1}: ").upper())
    entry = {customer_name: items}
    shopping_lists.update(entry)
    return entry

def add_customer():
    customer_name=input("Enter your name: ").capitalize()
    total_spend = -1
    while total_spend == -1:
        total_spend = input("Enter your total spend: ")
        if total_spend.isdigit():
            total_spend = int(total_spend)
        else:
            print("Enter a positive number.")
    record = {customer_name: total_spend}
    customer_details.update(record)
    return record
   
def print_large_spenders():
    for customer in customer_details:
        if customer_details[customer] > 200:
            print(customer, end=" ", flush=True)
    print() 

add_to_list()
add_customer()
print_large_spenders()

for i in range(5002, 5011, 2):
    print(i)

orders = [["OrderID","ProductName","Quantity"],[5001,"Laptop",1],[5002,"Mouse",2],[5003,"Keyboard",1]]
print(orders[2][1])
user_specified_id = get_number("Enter an order ID")
found = False
for order in orders:
    if user_specified_id in order:
        found = True
        print(order[1], order[2])
if not found:
    print("Item not found")