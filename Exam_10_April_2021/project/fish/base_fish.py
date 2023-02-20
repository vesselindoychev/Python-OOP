from abc import ABC, abstractmethod


class BaseFish(ABC):
    _INVALID_NAME_MESSAGE = "Fish name cannot be an empty string."
    _INVALID_SPECIES_MESSAGE = "Fish species cannot be an empty string."
    _INVALID_PRICE_MESSAGE = "Price cannot be equal to or below zero."
    _MIN_PRICE_VALUE = 0
    _INCREASE_SIZE = 5
    _WATER = ''

    @abstractmethod
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @classmethod
    def __validate_name(cls, value):
        if value == '':
            raise ValueError(cls._INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_species(cls, value):
        if value == '':
            raise ValueError(cls._INVALID_SPECIES_MESSAGE)

    @classmethod
    def __validate_price(cls, value):
        if value <= cls._MIN_PRICE_VALUE:
            raise ValueError(cls._INVALID_PRICE_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__validate_species(value)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    def eat(self):
        self.size += self._INCREASE_SIZE

    @property
    def fish_type(self):
        return self._WATER
