from Exam_10_April_2021.project import Fridge
from Exam_10_April_2021.project import Laptop
from Exam_10_April_2021.project import TV
from Exam_10_April_2021.project import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)
