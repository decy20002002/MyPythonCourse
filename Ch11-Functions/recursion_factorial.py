def calc_factorial(x, processed=""):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 0: #if x=1, return as 1
        print('Invalid Entry')
        return
    elif x == 1: #if x=1, return as 1
        print('processed ', processed)
        return 1
    else:
        if (processed): 
            processed = processed + " * " + str(x)
        else:
            processed = str(x)
        return (x * calc_factorial(x-1, processed))

num = 0
print("The factorial", num,"! is:", calc_factorial(num))