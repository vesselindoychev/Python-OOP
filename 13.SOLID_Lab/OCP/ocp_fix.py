from demo_project.exercise_plan import Rect, Triangle, Square
from demo_project.exercise_plan import Circle


class ShapesCalculator:
    def _calc_shape_area(self, shape):
        return shape.area()

    def calculate_areas_sum(self, shapes):
        return sum(self._calc_shape_area(s) for s in shapes)

    # Adding this is not a violation to OCP
    def calculate_perimeter(self, shapes):
        pass


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
    shapes_area_calculator = ShapesCalculator()
    printer = StdinPrinter()

    # printer = FilePrinter('./output.txt')

    def print_areas_sum(self, shapes):
        area_sum = self.shapes_area_calculator.calculate_areas_sum(shapes)
        self.printer.print(f'Area sum of shapes is: {area_sum}')


shapes = [
    Circle(10),
    Rect(4, 5),
    Triangle(2, 5),
    Square(4),
]

ShapesController().print_areas_sum(shapes)
