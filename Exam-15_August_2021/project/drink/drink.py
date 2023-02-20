from abc import ABC, abstractmethod

from Exam_10_April_2021.project import Validator


class Drink(ABC):
    _INVALID_NAME_MESSAGE = "Name cannot be empty string or white space!"
    _INVALID_PORTION_MESSAGE = "Portion cannot be less than or equal to zero!"
    _INVALID_BRAND_MESSAGE = "Brand cannot be empty string or white space!"

    @abstractmethod
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_exception_when_it_is_empty_string_or_white_space(value, self._INVALID_NAME_MESSAGE)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        Validator.raise_exception_when_it_is_0_or_less(value, self._INVALID_PORTION_MESSAGE)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.raise_exception_when_it_is_empty_string_or_white_space(value, self._INVALID_BRAND_MESSAGE)
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
