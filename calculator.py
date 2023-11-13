# calulator


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1 / num2


def multiplication(num1, num2):
    return num1 * num2


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
opt = input("Enter operator +,-,/,* : ")

if opt == "+":
    print(addition(num1, num2))
elif opt == "-":
    print(subtraction(num1, num2))
elif opt == "/":
    print(division(num1, num2))
elif opt == "*":
    print(multiplication(num1, num2))
else:
    print("Invalid Choice")
