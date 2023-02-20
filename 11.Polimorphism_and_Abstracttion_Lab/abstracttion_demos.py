from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'Area: {self.area()}; Perimeter: {self.perimeter()}'


class Triangle(Shape):
    def __init__(self, height, side):
        self.height = height
        self.side = side

    def area(self):
        return self.height * self.side

    def perimeter(self):
        return (self.height * self.side) / 2


#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def volume(self):
#         return self.height
#
#
def print_area(shape: Shape):
    print(shape.area())
    print(shape.perimeter())


shapes = [
    Triangle(1, 2),
    Triangle(2, 2),
    Triangle(3, 2),
    Triangle(4, 2)

]

for x in shapes:
    print(x)
