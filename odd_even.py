#  Write a program that asks the user for a number and determines whether it's odd or even.
#even = num % 2 == 0
#odd = num % 2 != 0 or num % 2 == 1 or num & 1

number = int(input("Enter Any Number : "))

if number & 1:
    print("Your Number Is Odd")
else:
    print("Your Number Is Even")
