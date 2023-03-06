from .computer import Computer

class Laptop(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        valid_processors = {
            'AMD Ryzen 9 5950X': 900,
            'Intel Core i9-11900H': 1050,
            'Apple M1 Pro': 1200
        }
        valid_ram_sizes = self.__valid_ram_sizes()
        is_processor_valid = self.__is_processor_valid(processor, valid_processors)
        is_ram_valid = self.__is_ram_valid(ram, valid_ram_sizes)

        if is_processor_valid and is_ram_valid:
            self.processor = processor
            self.ram = ram
            self.price = self.__create_price_by_ram(ram) + (valid_processors[processor])
            return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @staticmethod
    def __valid_ram_sizes():
        sizes = []
        for i in range(1, 7):
            sizes.append(2 ** i)
        return sizes

    def __is_processor_valid(self, processor, valid_processors):
        if processor not in valid_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        return True

    def __is_ram_valid(self, ram, valid_ram_sizes):
        if ram not in valid_ram_sizes:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        return True

    @staticmethod
    def __create_price_by_ram(ram):
        for i in range(1, 7):
            if 2 ** i == ram:
                return i * 100
