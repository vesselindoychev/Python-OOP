from Exam_10_April_2021.project import Fridge
from Exam_10_April_2021.project import Laptop
from Exam_10_April_2021.project import TV
from Exam_10_April_2021.project import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        count = 2 + len(children)
        super().__init__(family_name, salary_one + salary_two, count)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.calculate_expenses(self.appliances, self.children)
