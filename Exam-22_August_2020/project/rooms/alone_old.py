from Exam_10_April_2021.project import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, 1)
        self.room_cost = 10

