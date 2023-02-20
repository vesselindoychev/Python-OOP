from project.validator import Validator


class Race:
    _INVALID_NAME_MESSAGE = "Name cannot be an empty string!"

    def __init__(self, name):
        self.name = name
        self.drivers = []

    @classmethod
    def __validate_name(cls, value):
        if value.strip() == '':
            raise ValueError(cls._INVALID_NAME_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value
