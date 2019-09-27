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
print(rect_1.area_formula)
print(rect_2.area_formula)
rect_1.area_formula = "area = length*width"
print(rect_1.area_formula)
print(rect_2.area_formula)