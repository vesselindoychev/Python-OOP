from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.controller import Controller
from project.driver import Driver
from project.race import Race

controller = Controller()
# muscle_car = MuscleCar('Mustang GT', 260)
# sport_car1 = SportsCar('BMW e60', 500)
# sport_car2 = SportsCar('Audi A6', 500)
#
# driver1 = Driver('Patrick')
# race = Race('HotWheels Race')
#
# print(controller.create_car('SportsCar', 'BMW e60', 500))
# print(controller.create_car('SportsCar', 'Audi A6', 500))
# print(controller.create_car('MuscleCar', 'Mustang GT', 300))
# print(controller.create_car('MuscleCar', 'Mustang Shelby', 400))
#
# print(controller.create_driver('Patrick'))
#
# print(controller.create_race('HotWheels Race'))
# print(controller.add_car_to_driver('Patrick', 'SportsCar'))
# print(controller.add_car_to_driver('Patrick', 'SportsCar'))



print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))

print(controller.start_race("Christmas Top Racers"))