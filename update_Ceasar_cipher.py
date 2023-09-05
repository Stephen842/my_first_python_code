#Ceasar Cipher

text = input("Enter your message: ")
shift = 0

while shift == 0:
    try:
        shift = int(input("Eneter a cipher shift value: "))
        if shift not in range(1, 26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("incorrect shift value!")

cipher = ""

for i in text:
    if not i.isalpha():
        code = ord(i) + shift

        if i.isupper():
            first = ord("A")
        else:
            first = ord("a")

        code -= first
        code %= 26

        cipher += chr(first + code)
    else:
        cipher += i

print(i)

