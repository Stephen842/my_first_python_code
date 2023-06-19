#this program gives the tax levy given to citizen based on the requirement of their salary

income = float(input("enter your annual income: "))

if income < 300:
    tax = income * 0.18 - 30.02

if income > 300:
    tax = (income - 300) * 0.32 + 30.02

else:
    tax < 0.00
    tax = 0.00

print("your tax is ", round(tax, 0), "dollars")
