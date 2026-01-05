age = int(input("How old are you?\n>"))

if age<12:
    print("Child ticket: £5")
elif age<18:
    print("Teen ticket: £7")
else:
    print("Adult ticket: £10")