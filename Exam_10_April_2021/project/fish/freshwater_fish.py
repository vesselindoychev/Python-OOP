from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    _WATER = 'Fresh'
    _INCREASE_SIZE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += self._INCREASE_SIZE

    @property
    def WATER(self):
        return self._WATER
