from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    _INVALID_NAME_MESSAGE = "Aquarium name cannot be an empty string."
    _WATER = ''

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return f"Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):

        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        names = ''
        result = f'{self.name}:\n'
        if not self.fish:
            names = 'none'
        else:
            names = ' '.join([fish.name for fish in self.fish])

        result += f'Fish: {names}\n'
        result += f'Decorations: {len(self.decorations)}\n'
        result += f'Comfort: {self.calculate_comfort()}'
        return result

    @property
    def water_type(self):
        return self._WATER
