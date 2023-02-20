from project.race import Race
from project.driver import Driver
from project.car.sports_car import SportsCar
from project.car.muscle_car import MuscleCar


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_models = set()
        self.driver_names = set()
        self.race_names = set()

    def __find_car_by_type(self, car_type):
        cars = [car for car in self.cars if not car.is_taken and car_type == car.__class__.__name__]
        return cars[-1] if cars else None

    def __find_driver_by_name(self, driver_name):
        drivers = [driver for driver in self.drivers if driver.name == driver_name]
        return drivers[0] if drivers else None

    def __find_race_by_name(self, race_name):
        races = [race for race in self.races if race.name == race_name]
        return races[0] if races else None

    def create_car(self, car_type, model, speed_limit):
        if model in self.car_models:
            raise Exception(f"Car {model} is already created!")

        created_car = self.__create_car(car_type, model, speed_limit)
        self.cars.append(created_car)
        self.car_models.add(model)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if driver_name in self.driver_names:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        self.driver_names.add(driver_name)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if race_name in self.race_names:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        self.race_names.add(race_name)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        car = self.__find_car_by_type(car_type)
        driver = self.__find_driver_by_name(driver_name)

        if driver_name not in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        driver.car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        driver = self.__find_driver_by_name(driver_name)
        race = self.__find_race_by_name(race_name)

        if race_name not in self.race_names:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_name not in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__find_race_by_name(race_name)

        if race_name not in self.race_names:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers = sorted([driver for driver in race.drivers], key=lambda x: x.car.speed_limit, reverse=True)[0: 3]

        result = ''

        for d in drivers:
            d.number_of_wins += 1
            result += f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.\n"

        return result

    @staticmethod
    def __create_car(car_type, model, speed_limit):
        if car_type == MuscleCar.__name__:
            return MuscleCar(model, speed_limit)
        if car_type == SportsCar.__name__:
            return SportsCar(model, speed_limit)
