class Player:
    _INVALID_NAME_MESSAGE = "Name not valid!"
    _MIN_AGE_VALUE = 12
    _INVALID_AGE_MESSAGE = "The player cannot be under 12 years old!"
    _MAX_STAMINA_VALUE = 100
    _MIN_STAMINA_VALUE = 0
    _INVALID_STAMINA_MESSAGE = "Stamina not valid!"
    player_names = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @classmethod
    def __validate_age(cls, value):
        if value < cls._MIN_AGE_VALUE:
            raise ValueError(cls._INVALID_AGE_MESSAGE)

    @classmethod
    def __validate_stamina(cls, value):
        if value < cls._MIN_STAMINA_VALUE or value > cls._MAX_STAMINA_VALUE:
            raise ValueError(cls._INVALID_STAMINA_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError(self._INVALID_NAME_MESSAGE)
        if value in self.player_names:
            raise Exception(f"Name {value} is already used!")
        self.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__validate_stamina(value)
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self._MAX_STAMINA_VALUE
