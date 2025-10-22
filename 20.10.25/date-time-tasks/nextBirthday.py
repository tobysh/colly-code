import datetime
birthday = input("Enter your birthday in the format \"Day, Month\"").split(',')
if len(birthday) != 2:
    print("Invalid birthday")
else:
    for i in range(len(birthday)):
        birthday[i] = int(birthday[i].rstrip())
    print(birthday)

td = datetime.datetime(birthday[0], birthday[1], birthday[2]) - datetime.datetime.now()
print(td.days)