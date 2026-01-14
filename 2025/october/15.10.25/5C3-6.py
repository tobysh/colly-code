mark = int(input("Enter the mark (0-100): "))
if mark >= 70:
    print("Distinction")
elif mark >= 60 and mark < 69:
    print("Merit")
elif mark >= 50 and mark <= 59:
    print("Pass")
elif mark < 50:
    print("Fail")
else:
    print("Invalid")
