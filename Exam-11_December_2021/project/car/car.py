from abc import ABC, abstractmethod


class Car(ABC):
    _MIN_SPEED_LIMIT = None
    _MAX_SPEED_LIMIT = None
    _MIN_SYMBOL_LENGTH = 4
    _INVALID_SPEED_MESSAGE = None

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @classmethod
    def __validate_speed_limit(cls, value):
        if value < cls._MIN_SPEED_LIMIT:
            raise ValueError(cls._INVALID_SPEED_MESSAGE)
        if value > cls._MAX_SPEED_LIMIT:
            raise ValueError(cls._INVALID_SPEED_MESSAGE)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < self._MIN_SYMBOL_LENGTH:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value
