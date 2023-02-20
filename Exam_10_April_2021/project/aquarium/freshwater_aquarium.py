from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _WATER = 'Fresh'

    def __init__(self, name):
        super().__init__(name, capacity=50)
