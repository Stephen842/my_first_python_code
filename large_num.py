#this program give the largest number by comparing between 3 given digits

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

larger_num = number1

if number2 > larger_num:
    larger_num = number2

if number3 > larger_num:
    larger_num = number3

print("the largest number is: ", larger_num)
