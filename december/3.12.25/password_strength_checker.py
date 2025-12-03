password = input("Enter your password: ").strip()
length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
has_capital = any(char.isupper() for char in password)
print(f"""
      8 or more characters: {length}
      Contains a capital letter: {has_capital}
      Contains a number: {has_number}
      """)