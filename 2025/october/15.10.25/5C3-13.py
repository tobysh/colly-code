while True:
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")
    
    choice = (input("Choose an option: "))
    
    if choice == "5":
        break
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        result = a + b
        print("Sum:", result)
    elif choice == "2":
        result = a - b
        print("Difference:", result)
    elif choice == "3":
        print("Product:" + str(a * b))
    elif choice == "4":
        if b == 0:
            print("Error: Division by zero not allowed")
        else:
            print("Quotient:", str(a / b))
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Invalid option, try again.")
