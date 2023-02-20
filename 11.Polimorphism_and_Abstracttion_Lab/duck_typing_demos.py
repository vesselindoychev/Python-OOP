class Item:
    def sound(self):
        pass

    def eat(self):
        return 'eating'

    def work(self):
        return 'working...'


class Cat(Item):
    def sound(self):
        return 'Meow...'


class Dog(Item):
    def sound(self):
        return 'Bark, bark...'


class Person(Item):
    # def eat(self):
    #     return super().eat()

    def sound(self):
        return '@$#@%@#!!#$'


def play_sound(item_sound: Item):
    print(item_sound.sound())
    print(item_sound.eat())
    print(item_sound.work())


cat = Cat()
p = Person()
play_sound(cat)
play_sound(p)
