import sys

try:
    arg_string1=sys.argv[1]
    arg_string2=sys.argv[2]
except IndexError:
    print('Invalid input, please enter two whole numbers')
    sys.exit(-1)

#after inputs work
try:
    arg1 = int(arg_string1)
    arg2 = int(arg_string2)
    #total = arg1 + arg2
    #print('Total is:', total)
except ValueError:
    print('Invalid input, please enter two whole numbers')
    sys.exit(-1)
total = arg1 + arg2
print('Total is:', total)
