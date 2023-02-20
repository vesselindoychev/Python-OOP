from abc import ABC, abstractmethod

from project.validator import Validator


class BakedFood(ABC):
    _INVALID_NAME_MESSAGE = "Name cannot be empty string or white space!"
    _INVALID_PRICE_MESSAGE = "Price cannot be less than or equal to zero!"

    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_exception_when_value_is_empty_string_or_whitespace(value, self._INVALID_NAME_MESSAGE)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_exception_when_value_is_0_or_less(value, self._INVALID_PRICE_MESSAGE)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
