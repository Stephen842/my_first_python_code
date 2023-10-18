#IBAN validator

iban = input("Enter Your IBAN Value: ")
iban = iban.replace(" ", "")
if not iban.isalnum():
    print("invalid IBAN Value inputted")
elif len(iban) < 15:
    print("IBAN value too short")
elif len(iban) > 31:
    print("IBAN value too long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ""

    for i in iban:
        if i.isdigit():
            iban2 += i
        else:
            iban2 += str(10 + ord(i) - ord("A"))
    iban = int(iban2)

    if iban % 97 == 1:
        print("The Value inputted is correct")
    else:
        print("Invalid IBAN Inputed")

