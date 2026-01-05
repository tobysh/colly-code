import string
sentence = input("Enter your string to see if it\'s a palindrome: ").strip().lower()
(sentence.translate(str.maketrans('', '', string.punctuation))).replace(" ","")
if sentence[::-1] == sentence:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
