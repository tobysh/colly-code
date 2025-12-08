import string

alphabet = string.ascii_lowercase

sentence = input("Enter your string to be encoded: ")
shift = None
while shift == None:
    inp = input("Enter the amount of characters to shift the string by: ")
    try:
        shift = int(inp)
    except ValueError:
        print("Enter a valid number.")

keyword = []

if 0 < shift <= 26:
    for letter in sentence:
        get_letter = alphabet.index(letter) + shift	
        keyword.append(alphabet[get_letter])
    print("".join(keyword))
else:
    print("Key must be between 1 and 26!")