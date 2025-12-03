import re

def validate_number(number):
    valid = True
    if "+" not in number:
        try:
            int(number)
        except ValueError:
            print("Invalid number, contains letters")
            valid = False
        if len(number) > 14:
            print("Number is too long")
            valid = False
        elif len(number) > 11:
            print("Number needs a country code for this length")
            valid = False
        elif len(number) == 11:
            if number[0] != "0":
                print("Numbers of this length need a 0 at the start")
                valid = False
        elif len(number) != 10:
            print("Number length is invalid")
            valid = False
    elif "+" in number:
        if number.count("+") > 1:
            print("Only 1 \"+\" is allowed")
            valid = False
        if number[0] != "+":
            print("The country code must be at the start if a \"+\" is included")
            valid = False
        if not (len(number) == 13 or len(number) == 14):
            print("Invalid length for a number with a country code")
            valid = False
        else:
            try:
                int(re.sub("\+", "", number))
            except ValueError:
                print("Invalid number, contains letters")
                valid = False
            if len(number) == 14:
                if number[2] != "0":
                    print("Numbers of this length need a 0 at the start of the actual number")
                    valid = False
    return valid
    


name = input("Enter your name: ").strip()
phone_number = input("Enter your phone number: ")
phone_number = re.sub(" ", "", phone_number)

if not validate_number(phone_number):
    print("Invalid mobile number")
elif name == "":
    print("Invalid name")
else:    
    print(f"Hello, {name}, your number is {phone_number}")