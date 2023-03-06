from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0
        self.valid_types = ['Laptop', 'DesktopComputer']

    @abstractmethod
    def configure_computer(self, processor, ram):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError('Model name cannot be empty.')
        self.__model = value