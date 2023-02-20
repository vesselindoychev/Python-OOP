from Exam_10_April_2021.project import TV
from Exam_10_April_2021.project import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
        self.appliances = [TV()]
        self.room_cost = 10
        self.calculate_expenses(self.appliances)
