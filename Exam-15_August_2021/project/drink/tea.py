from Exam_10_April_2021.project import Drink


class Tea(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 2.50, brand)