# Create a Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate and return the area
    def calculate_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}")

    # Method to calculate and return the perimeter
    def calculate_perimeter(self):
        perimeter = (self.length + self.width) * 2
        print(f"The perimeter of the rectangle is {perimeter}")


# Create objects and display area and perimeter
rect_1 = Rectangle(10, 2)
rect_1.calculate_area()
rect_1.calculate_perimeter()

rect_2 = Rectangle(3, 4)
rect_2.calculate_area()
rect_2.calculate_perimeter()
