class Rectangle():
    """Holds width and length and calculates area."""
    area_formula = "area = length * width"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

newRectangle = Rectangle(12,10)
print(newRectangle.area())

rect_1 = Rectangle(2,8)
rect_2 = Rectangle(4,5)
rect_3 = Rectangle(3,22)

print(rect_1.area_formula)
print(rect_2.area_formula)
rect_1.area_formula = "area = length*width"
print(rect_1.area_formula)
print(rect_2.area_formula)

Rectangle.area_formula = "area = length*width"
print(rect_2.area_formula)
print(rect_3.area_formula)