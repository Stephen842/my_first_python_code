#palindromes

user = input("Enter your Message: ")
user = user.replace(" ", "")

if len(user) > 1 and user.upper() == user[:: -1].upper():
    print("this is a palindromes")
else:
    print("this is not a palindromes")

