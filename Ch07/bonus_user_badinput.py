import sys

try:
    
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    Division = num1 / num2
    
except ZeroDivisionError:
    print('Divide by ZERO is unacceptable!')
    sys.exit(-1)

print('Total number after division:', Division)