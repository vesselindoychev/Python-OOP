from Exams.project.astronaut.astronaut_repository import AstronautRepository
from Exams.project.astronaut.biologist import Biologist
from Exams.project.astronaut.geodesist import Geodesist
from Exams.project.astronaut.meteorologist import Meteorologist
from Exams.project.planet.planet import Planet
from Exams.project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.__creates_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.find_most_suitable_astronauts_for_mission(5, 30)

        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_astronauts = 0

        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if len(planet.items) == 0:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participated_astronauts} " \
                   f"astronauts participated in collecting items."
        else:
            self.failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f'{self.successful_missions} successful missions!' + '\n'
        result += f'{self.failed_missions} missions were not completed!' + '\n'
        result += "Astronauts' info:" + '\n'
        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + '\n'

        return result.strip()

    @staticmethod
    def __creates_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")
