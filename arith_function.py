#this program uses a function to perform some basic arithmetic between two interger values


#this program give the sum of numbers by addtion
def add():
    addition = a + b
    print("the addition of", a , "to", b, "is", addition)

a = int(input("enter a value for a: "))
b = int(input("enter a value for b: "))

add()


#this program gives the difference between numbers by dividing
def sub():
    subtraction = a - b
    print("the difference between", a , "to", b, "is", subtraction)

a = int(input("enter a value for a: "))
b = int(input("enter a value for b: "))

sub()

#this program multiply two given numbers
def mul():
    multiply = a * b
    print("the multiple of", a , "to", b, "is", multiply)

a = int(input("enter a value for a: "))
b = int(input("enter a value for b: "))

mul()

#this program divide two given numbers
def div():
    divide = a / b
    print("the division of", a , "and", b, "is", divide)

a = int(input("enter a value for a: "))
b = int(input("enter a value for b: "))

div()
