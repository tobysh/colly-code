mark = int(input("What mark did you get on the test?\n>"))
if mark < 1:
    print("Invalid score")
elif mark < 50:
    print("Needs improvement.")
elif mark <70:
    print("Good effort.")
else:
    print("Excellent!")