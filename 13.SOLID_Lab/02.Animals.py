class Animal:
    _species = None
    _sound = None

    def get_species(self):
        return self._species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = 'meow'
    _species = 'cat'


class Dog(Animal):
    _sound = 'woof-woof'
    _species = 'dog'

class Chicken(Animal):
    _sound = 'cluck'
    _species = 'chicken'

def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)


