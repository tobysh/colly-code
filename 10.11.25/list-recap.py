import os
shopping_list=["apples", "bananas"]
for i in range(5):
    os.system('clear')
    for item in shopping_list:
        print(item, end=", ")
    print()
    shopping_list.append(input("Enter an item to add to the shopping list\n>").lower())

shopping_list.append("milk")
try:
    shopping_list.remove("bread")
except ValueError:
    print("Bread is not in the list")
print(len(shopping_list))
shopping_list.sort()
for item in shopping_list:
    print(item, end=", ")
print()