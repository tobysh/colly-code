correct_pin = "1122"
attempts = 0
max_attempts = 4

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Incorrect PIN")

if attempts == max_attempts:
    print("Card blocked")