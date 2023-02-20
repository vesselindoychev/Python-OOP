from Exam_10_April_2021.project import BakedFood


class Bread(BakedFood):
    def __init__(self, name, price):
        super().__init__(name, 200, price)
