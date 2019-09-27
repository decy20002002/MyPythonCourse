#define a class
class Square1:
    side = 5

#instantiating an object
some_square = Square1()
print(some_square.side)

#-------------------------------

#define a class
class Square2:
    #define function in class 
    # __init__ everytime the class is being used to create a new object
    #(self,...) refers to the created object
    def __init__(self, side):
        self.side = side
        #self.color = color

#instantiating an object passing value to Square2
some_square = Square2(10)
#some_square = Square2("Red")
print(some_square.side)

#-------------------------------

#define a class
class Square3:
    def __init__(self, side):
        self.side = side
    
    def calc_area(self):
        return self.side**2

some_square = Square3(10)
print(some_square.calc_area())


