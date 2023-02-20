from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def __find_aquarium_by_name(self, name):
        aquariums = [aquarium for aquarium in self.aquariums if aquarium.name == name]
        return aquariums[0] if aquariums else None

    def add_aquarium(self, aquarium_type, aquarium_name):
        aquarium = self.__create_aquarium(aquarium_type, aquarium_name)

        if isinstance(aquarium, str):
            return aquarium

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        decoration = self.__create_decoration(decoration_type)
        if isinstance(decoration, str):
            return decoration
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium is not None:
            aquarium.decorations.append(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)
        if isinstance(fish, str):
            return fish

        if aquarium.water_type != fish.fish_type:
            return f"Water not suitable."
        if aquarium.capacity <= len(aquarium.fish):
            return f"Not enough capacity."

        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            value = sum(decoration.price for decoration in aquarium.decorations) + sum(
                fish.price for fish in aquarium.fish)
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += f'{str(aquarium)}\n'
        return result.strip()

    @staticmethod
    def __create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == FreshwaterAquarium.__name__:
            return FreshwaterAquarium(aquarium_name)
        if aquarium_type == SaltwaterAquarium.__name__:
            return SaltwaterAquarium(aquarium_name)
        return "Invalid aquarium type."

    @staticmethod
    def __create_decoration(decoration_type):
        if decoration_type == Ornament.__name__:
            return Ornament()
        if decoration_type == Plant.__name__:
            return Plant()
        return f"Invalid decoration type."

    @staticmethod
    def __create_fish(fish_type, fish_name, fish_species, price):
        if fish_type == FreshwaterFish.__name__:
            return FreshwaterFish(fish_name, fish_species, price)
        if fish_type == SaltwaterFish.__name__:
            return SaltwaterFish(fish_name, fish_species, price)
        return f"There isn't a fish of type {fish_type}."
