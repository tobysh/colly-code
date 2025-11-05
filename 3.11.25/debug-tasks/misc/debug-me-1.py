mark = int(input("Enter a mark between 0 and 100: "))
while mark < 0 or mark > 100:
    print("Invalid mark.")
    mark = int(input("Enter a mark between 0 and 100: "))
print("Valid mark")