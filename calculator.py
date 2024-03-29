#!/bin/pyhon3

import math
#1. ADD
#2. SUBTRACT
#3. MULTIPLY
#4. DIVIDE
#5. SQUARE ROOT
#6. RAISE TO POWER

#Add a pretty banner
print("_" * 50)
print("Calculator creator: Javis Wahome")
print("_" * 50)

print("select an operation to perform:")
print("1 ADD")
print("2 SUBTRACT")
print("3 MULTIPLY")
print("4 DIVIDE")
print("5 SQUARE ROOT")
print("6 RAISE TO POWER")

operation = input()

if operation == "1": #perfomrs addition
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	print(" The sum is " + str(int(num1) + int(num2)) )
elif operation == "2": #performs subtraction
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	print("The difference is " + str(int(num1) - int(num2)) )
elif operation  == "3": #performs multiplication
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	print("The product is " + str(int(num1) * int(num2)) )
elif operation == "4": #perform division
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	print("The result is " + str(int(num1) / int(num2)) )
elif operation == "5": #perform square root
	num = int(input("Enter number: "))
	print("The square root is %f " %(math.sqrt(num)) )
elif operation == "6": #perform power
	num = int(input("Enter number: "))
	print("The result is %f " %(pow(num, 2)))
else:
	print("Invalid entry")
