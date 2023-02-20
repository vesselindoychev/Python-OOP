from abc import ABC, abstractmethod

from Exam_10_April_2021.project import BakedFood
from Exam_10_April_2021.project import Drink
from Exam_10_April_2021.project import Validator


class Table(ABC):
    _INVALID_CAPACITY_MESSAGE = "Capacity has to be greater than 0!"

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def __clear_initialization(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_exception_when_it_is_0_or_less(value, self._INVALID_CAPACITY_MESSAGE)
        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        price_of_food_orders = [f.price for f in self.food_orders]
        price_of_drink_orders = [d.price for d in self.drink_orders]
        return sum(price_of_food_orders) + sum(price_of_drink_orders)

    def clear(self):
        self.__clear_initialization()

    def free_table_info(self):
        if self.is_reserved:
            return None
        result = f"Table: {self.table_number}" + '\n'
        result += f"Type: {self.table_type}" + '\n'
        result += f"Capacity: {self.capacity}"

        return result

    @property
    @abstractmethod
    def table_type(self):
        pass
