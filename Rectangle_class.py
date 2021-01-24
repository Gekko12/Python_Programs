"""
Program to express instances as return values to define a class Rectangle with members
width, height, corner_x, corner_y and member function to find centre, area and perimeter
of a rectangle.
"""


class Rectangle:
    def __init__(self, width, height, corner_x, corner_y):
        self.width = width
        self.height = height
        self.corner_x = corner_x
        self.corner_y = corner_y

    def __str__(self):
        """" This function returns the centre points(x,y)"""
        return "centre_x = "+str(self.corner_x)+", centre_y = "+str(self.corner_y)

    def find_centre(self):
        x = self.corner_x + self.width / 2.0
        y = self.corner_y + self.height / 2.0
        rec = Rectangle(0, 0, x, y)
        return rec

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)


obj = Rectangle(100, 20, 50, 50)
print("Centre points :",obj.find_centre())
print("Area = ",obj.area())
print("Perimeter = ",obj.perimeter())