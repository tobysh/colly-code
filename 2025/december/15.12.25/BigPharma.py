
import datetime

medicines = {}
customers = {}
sales = []

def add_medicine(med_id, name, price, quantity, expiry_date):
    if not quantity.isdigit():
        print("Quantity must be a positive integer.")
    elif not med_id.isdigit():
        print("Medicine ID must be a positive integer.")
    else:
        try:
            medicines[med_id] = {
                "name": name,
                "price": float(price),
                "quantity": int(quantity),
                "expiry": expiry_date
            }
            print(f"Medicine '{name}' added successfully.")
        except ValueError as e:
            print(f"Invalid details inputted. ({e})")


def view_medicines():
    print("\n--- Medicine Stock ---")
    for mid in medicines:
        m = medicines[mid]
        print(mid, m["name"], "£", m["price"], "Qty:", m["quantity"], "Expiry:", m["expiry"])


def add_customer(cust_id, name):
    if not cust_id.isdigit(): 
        print("Customer ID must be a positive integer.")
    elif not name.isalpha():
        print("Customer name must not contain numbers or symbols.")
    else:
        customers[cust_id] = {
                "name": name,
                "purchases": []
            }
        print(f"Customer '{name}' added.")


def view_customers():
    print("\n--- Customers ---")
    for cid, c in customers.items():
        print(cid, c["name"], "Purchases:", len(c["purchases"]))


def sell_medicine(cust_id, med_id, quantity):


    quantity = int(quantity)
    total_cost = medicines[med_id]["price"] * quantity

    medicines[med_id]["quantity"] -= quantity

    sale = {
        "customer": cust_id,
        "medicine": med_id,
        "quantity": quantity,
        "total": total_cost,
        "date": datetime.date.today()
    }

    sales.append(sale)
    customers[cust_id]["purchases"].append(sale)

    print("Sale completed. Total cost: £", total_cost)


def view_sales():
    print("\n--- Sales Report ---")
    for s in sales:
        print(s["date"], customers[s["customer"]]["name"], "bought",
              medicines[s["medicine"]]["name"], "x", s["quantity"],
              "Total: £", s["total"])


def low_stock_report():
    print("\n--- Low Stock Medicines ---")
    for mid in medicines:
        if medicines[mid]["quantity"] < 5:
            print(medicines[mid]["name"], "is low on stock!")


def menu():
    while True:
        print("\n===== PHARMACY MANAGEMENT SYSTEM =====")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Sell Medicine")
        print("6. View Sales")
        print("7. Low Stock Report")
        print("8. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            mid = input("Medicine ID: ")
            name = input("Name: ")
            price = input("Price (£): ")
            qty = input("Quantity: ")
            expiry = input("Expiry Date (YYYY-MM-DD): ")
            add_medicine(mid, name, price, qty, expiry)

        elif choice == "2":
            view_medicines()

        elif choice == "3":
            cid = input("Customer ID: ")
            name = input("Customer Name: ")
            add_customer(cid, name)

        elif choice == "4":
            view_customers()

        elif choice == "5":
            cid = input("Customer ID: ")
            mid = input("Medicine ID: ")
            qty = input("Quantity: ")
            sell_medicine(cid, mid, qty)

        elif choice == "6":
            view_sales()

        elif choice == "7":
            low_stock_report()
        elif choice == "8":
            print("Exiting system...")
            break

        else:
            print("Invalid option")


menu()
