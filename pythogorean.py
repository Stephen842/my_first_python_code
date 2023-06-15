#this program gives the result of a hypotenuse by doing some basic arithmetic

adj = float(input("Enter a number to be your adjacent value: "))
opp = float(input("Enter a number to be your opposite value: "))

hyp = (adj ** 2 + opp ** 2) ** 0.5
print("length of hypotenuse is: ", + str(hyp))
