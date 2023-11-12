import math


class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def c_square(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        square = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return square


t = Triangle(10, 4, 10)

type_of_t = t.get_type()
square = t.c_square()

print("Тип треугольника:", type_of_t)
print("Площадь треугольника:", square)