from demo_project.exercise_plan import Rect
from demo_project.exercise_plan import Circle
import math


class ShapesAreaCalculator:
    def _calc_shape_area(self, shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi

    def calculate_areas_sum(self, shapes):
        return sum(self._calc_shape_area(s) for s in shapes)


class StdinPrinter:
    def print(self, message):
        print(message)


class FilePrinter:
    def __init__(self, filename):
        self.filename = filename

    def print(self, message):
        with open(self.filename, 'a') as file:
            file.writelines([message])


class ShapesController:
    shapes_area_calculator = ShapesAreaCalculator()
    # printer = StdinPrinter()
    printer = FilePrinter('./output.txt')

    def print_areas_sum(self, shapes):
        area_sum = self.shapes_area_calculator.calculate_areas_sum(shapes)
        self.printer.print(f'Area sum of shapes is: {area_sum}')


shapes = [
    Circle(10),
    Rect(4, 5),
]

ShapesController().print_areas_sum(shapes)
