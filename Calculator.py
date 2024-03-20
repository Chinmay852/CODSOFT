def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

num1=float(input("Enter your first value: "))
num2=float(input("Enter the second value: "))
operand=(input("Choose operand(+,-,*,/): "))

if operand =='+':
    print("Result:",add(num1,num2))

if operand =='-':
    print("Result:", subtract(num1, num2))

if operand =='*':
    print("Result:", multiply(num1, num2))

if operand =='/':
    print("Result:", division(num1, num2))