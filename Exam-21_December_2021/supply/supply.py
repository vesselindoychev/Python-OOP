from abc import ABC, abstractmethod


class Supply(ABC):
    _INVALID_NAME_MESSAGE = "Name cannot be an empty string."
    _MIN_ENERGY_VALUE = 0
    _INVALID_ENERGY_MESSAGE = "Energy cannot be less than zero."

    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @classmethod
    def __validate_name(cls, value):
        if value == '':
            raise ValueError(cls._INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_energy(cls, value):
        if value < cls._MIN_ENERGY_VALUE:
            raise ValueError(cls._INVALID_ENERGY_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__validate_energy(value)
        self.__energy = value
