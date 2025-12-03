#Take a string input of a number and convert it to int, float, and str. Show the type of each.

numstring = input("Enter a number: ")
numint = int(numstring)
numfloat = float(numstring)

print(f"""
String: \"{numstring}\", {type(numstring).__name__}
Float: {numfloat}, {type(numfloat).__name__}
Int: {numint}, {type(numint).__name__}
      """)