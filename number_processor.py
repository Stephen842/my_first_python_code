#Number processor:

value = input("Enter numbers seperating them with a whitespace: ")
string = value.split()
total = 0
try:
    for i in string:
        total += float(i)
    print("the total value is ", total)
except:
    print(i, "is not a number")

