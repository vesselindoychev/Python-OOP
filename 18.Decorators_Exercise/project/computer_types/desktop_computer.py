from .computer import Computer

class DesktopComputer(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        available_processors = {
            'AMD Ryzen 7 5700G': 500,
            'Intel Core i5-12600K': 600,
            'Apple M1 Max': 1800
        }

        ram_sizes = self.__valid_max_sizes()
        is_processor_valid = self.__is_processor_available(processor, available_processors)
        is_ram_valid = self.__is_ram_valid(ram_sizes, ram)

        if is_processor_valid and is_ram_valid:
            self.processor = processor
            self.ram = ram
            self.price = self.__create_price_by_ram(ram) + available_processors[processor]
            return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    @staticmethod
    def __valid_max_sizes():
        sizes = []
        for i in range(1, 8):
            sizes.append(2 ** i)
        return sizes

    def __is_processor_available(self, processor, available_processors):
        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        return True

    def __is_ram_valid(self, ram_sizes, ram):
        if ram not in ram_sizes:
            raise ValueError(f"{self.ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        return True

    @staticmethod
    def __create_price_by_ram(ram):
        for i in range(1, 7):
            if 2 ** i == ram:
                return i * 100