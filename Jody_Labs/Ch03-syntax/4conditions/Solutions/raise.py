import sys

salary = int(input("How much of a raise will you give me?"))

if (salary < 0):
    sys.exit("that data is not good")
else:
    print('Let me consider it')
