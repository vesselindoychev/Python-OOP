from Exam_10_April_2021.project import Drink


class Water(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 1.50, brand)
