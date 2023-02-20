from Exam_10_April_2021.project import Table


class InsideTable(Table):
    _MIN_TABLE_NUMBER = 1
    _MAX_TABLE_NUMBER = 50
    _INVALID_TABLE_NUMBER_MESSAGE = "Inside table's number must be between 1 and 50 inclusive!"

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @classmethod
    def __validate_table_number(cls, value):
        if value < cls._MIN_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        if value > cls._MAX_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)

    @property
    def table_type(self):
        return 'InsideTable'

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value
