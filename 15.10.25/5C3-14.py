marks = []
run = True

while run:
    print("1. Enter marks for a student")
    print("2. Calculate average")
    print("3. Show highest and lowest mark")
    print("4. Exit")

    choice = (input("Enter choice: "))

    if choice == "1":
        m = int(input("Enter mark: "))
        marks = marks.append(m)
    elif choice == "2":
        if len(marks) != 0:
            total = sum(marks)
            avg = total / len(marks)
            print("Average mark is " + avg)
        else:
            print("Cannot divide by 0")
    elif choice == "3":
        high = max(marks)
        low = min(marks)
        print("Highest:", high)
        print("Lowest:", low)
    elif choice == "4":
        run == False
    else:
        print("Invalid choice, please try again")
