#find a word

word = input("Enter the word you need to find: ")
strn = input("Enter the strings you want to search through: ")

found = True
start = 0

for i in word:
    posit = strn.find(i, start)
    if posit < 0:
        found = False
        break
    start = posit + 1
if found:
    print("Yes")
else:
    print("No")

