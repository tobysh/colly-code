itemsList = input("Enter a list of items seperated by a comma: ").replace(' ','').split(',')
itemsListString = str(itemsList).replace(',', ' and').replace('\'', '').replace('[','').replace(']','')
print(itemsListString)