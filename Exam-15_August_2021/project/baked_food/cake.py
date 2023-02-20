from Exam_10_April_2021.project import BakedFood


class Cake(BakedFood):
    def __init__(self, name, price):
        super().__init__(name, 245, price)
