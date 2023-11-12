class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(15, 10)
square = r.square()
perimeter = r.perimeter()
print("Площадь:", square)
print("Периметр:", perimeter)