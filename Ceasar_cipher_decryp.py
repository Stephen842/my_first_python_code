#Ceasar cipher - decrypting a message

cipher = input("Enter your cryptogram: ")
value = ""

for i in cipher:
    if not i.isalpha():
        continue
    i = i.upper()
    code = ord(i) - 1
    if code < ord("A"):
        code = ord("Z")
    value += chr(code)
print(value)

