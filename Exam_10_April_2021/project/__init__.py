from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.plant import Plant

controller = Controller()

print(controller.add_aquarium('FreshwaterAquarium', 'Nemo'))

print(controller.add_fish('Nemo', 'FreshwaterFish', 'Frosty', 'Sharan', 20))
print(controller.add_fish('Nemo', 'FreshwaterFish', 'Fast', 'Sharan', 20))
print(controller.feed_fish('Nemo'))
print(controller.add_fish('Nemo', 'FreshwaterFish', 'Beta', 'Sharan', 20))
print(controller.add_fish('Nemo', 'FreshwaterFish', 'Lora', 'Sharan', 20))
print(controller.feed_fish('Nemo'))

print(controller.add_decoration('Plant'))
print(controller.feed_fish('Nemo'))
print(controller.insert_decoration('Nemo', 'Plant'))
print(controller.calculate_value('Nemo'))
controller.add_aquarium('SaltwaterAquarium', 'Zeus')
print(controller.report())
