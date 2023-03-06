from .computer_types.laptop import Laptop
from .computer_types.desktop_computer import DesktopComputer

class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer == 'Laptop':
            computer = Laptop(manufacturer, model)
            self.warehouse.append(computer)
            result = computer.configure_computer(processor, ram)
            return result
        elif type_computer == 'DesktopComputer':
            computer = DesktopComputer(manufacturer, model)
            self.warehouse.append(computer)
            result = computer.configure_computer(processor, ram)
            return result
        raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                price_difference = client_budget - computer.price
                self.profits += price_difference
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
        raise Exception(f"Sorry, we don't have a computer for you.")


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))