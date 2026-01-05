string = input("Enter a string to quantify the amount of vowels: ")
count = 0
for letter in string:
    if letter in ['a','e','i','o','u']:
        count = count+1
print(count)
