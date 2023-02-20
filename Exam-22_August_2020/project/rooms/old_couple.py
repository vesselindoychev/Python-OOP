from Exam_10_April_2021.project import Fridge
from Exam_10_April_2021.project import Stove
from Exam_10_April_2021.project import TV
from Exam_10_April_2021.project import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
