import math

from demo_project.exercise_plan import Rect
from demo_project.exercise_plan import Circle

# SRP (Single Responsibility Principle) Violations
"""class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def register(self, student):
        return student.id"""

# Avoiding SRP Violations

"""class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRecords:
    def get_student(self, id):
        pass

    def register(self, student):
        pass"""


class ShapesController:

    def _calc_shape_area(self, shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi

    # Violation of SRP, 2 responsibilities
    # - Calc of area sum
    # - Printing the sum
    def print_areas_sum(self, shapes):

        area_sum = sum(self._calc_shape_area(s) for s in shapes)

        print(f'Area sum of shapes is: {area_sum}')


shapes = [
    Circle(10),
    Rect(4, 5),
]

ShapesController().print_areas_sum(shapes)
