#Ceasar Cipher

value = input("Enter your message: ")
cipher = ""
for i in value:
    if not i.isalpha():
        continue
    i = i.upper()
    code = ord(i) + 1
    if code > ord("Z"):
        code = ord("A")
    cipher += chr(code)
print(cipher)
