#. Write a Python class named Rectangle constructed from length and width
# and a method that will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print("Area of the rectangle:", rect.area())
