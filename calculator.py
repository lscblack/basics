# calculator


def addition(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
opt = input("Enter Operator +,/,-,*: ")

if opt == "+":
    print(addition(num1, num2))
elif opt == "-":
    print(sub(num1, num2))
elif opt == "*":
    print(multi(num1, num2))
elif opt == "/":
    print(div(num1, num2))
else:
    print("Invalid Choice: ")