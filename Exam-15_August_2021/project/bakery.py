from Exam_10_April_2021.project import Bread
from Exam_10_April_2021.project import Cake
from Exam_10_April_2021.project import Water
from Exam_10_April_2021.project import Tea
from Exam_10_April_2021.project import InsideTable

from Exam_10_April_2021.project import OutsideTable
from Exam_10_April_2021.project import Validator


class Bakery:
    _INVALID_NAME_MESSAGE = "Name cannot be empty string or white space!"

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.food_menu_names = set()
        self.drinks_menu = []
        self.drinks_menu_names = set()
        self.tables_repository = []
        self.table_numbers = set()
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_exception_when_it_is_empty_string_or_white_space(value, self._INVALID_NAME_MESSAGE)
        self.__name = value

    def __get_table_by_number(self, table_number):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        return tables[0] if tables else None

    def __get_food_by_name(self, name):
        food = [f for f in self.food_menu if f.name == name]
        return food[0] if food else None

    def __get_drink_by_name(self, name):
        drinks = [d for d in self.drinks_menu if d.name == name]
        return drinks[0] if drinks else None

    def add_food(self, food_type, name, price):
        if name in self.food_menu_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.__create_food(food_type, name, price)
        self.food_menu.append(food)
        self.food_menu_names.add(name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in self.drinks_menu_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.__create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        self.drinks_menu_names.add(name)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in self.table_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.__create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        self.table_numbers.add(table_number)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        free_tables = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people]

        if not free_tables:
            return f"No available table for {number_of_people} people"
        table_to_be_reserved = free_tables[0]
        table_to_be_reserved.reserve(number_of_people)
        return f"Table {table_to_be_reserved.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        food_names_in_menu = [food_name for food_name in args if food_name in self.food_menu_names]
        food_names_not_in_menu = [food_name for food_name in args if food_name not in self.food_menu_names]

        available_food_object = [self.__get_food_by_name(f) for f in args if f in food_names_in_menu]
        [table.order_food(f) for f in available_food_object]

        ordered_food = '\n'.join(repr(f) for f in available_food_object)
        not_available_food = '\n'.join(food_names_not_in_menu)

        result = f'Table {table_number} ordered:' + '\n'
        result += ordered_food + '\n'
        result += f'{self.name} does not have in the menu:' + '\n'
        result += not_available_food

        return result

    def order_drink(self, table_number, *args):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        drink_names_in_menu = [drink_name for drink_name in args if drink_name in self.drinks_menu_names]
        drink_names_not_in_menu = [drink_name for drink_name in args if drink_name not in self.drinks_menu_names]

        available_drink_object = [self.__get_drink_by_name(d) for d in args if d in drink_names_in_menu]
        [table.order_food(d) for d in available_drink_object]

        ordered_drink = '\n'.join(repr(d) for d in available_drink_object)
        not_available_drink = '\n'.join(drink_names_not_in_menu)

        result = f'Table {table_number} ordered:' + '\n'
        result += ordered_drink + '\n'
        result += f'{self.name} does not have in the menu:' + '\n'
        result += not_available_drink

        return result

    def leave_table(self, table_number):
        table = self.__get_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        result = f'Table: {table_number}' + '\n'
        result += f'Bill: {table_bill:.2f}'

        return result

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        result = '\n'.join(table.free_table_info() for table in free_tables)
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def __create_food(food_type, name, price):
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)

    @staticmethod
    def __create_drink(drink_type, name, portion, brand):
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)

        if drink_type == Water.__name__:
            return Water(name, portion, brand)

    @staticmethod
    def __create_table(table_type, table_number, capacity):
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)
