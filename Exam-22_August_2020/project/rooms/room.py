from Exam_10_April_2021.project import Appliance
from Exam_10_April_2021.project import Child


class Room:
    _MAX_INVALID_NUMBER = 0
    _INVALID_EXPENSES_MESSAGE = "Expenses cannot be negative"

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < self._MAX_INVALID_NUMBER:
            raise ValueError(self._INVALID_EXPENSES_MESSAGE)
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_el in args:
            for el in list_el:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                elif isinstance(el, Child):
                    total_expenses += el.cost * 30

        self.expenses = total_expenses
