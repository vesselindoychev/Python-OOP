class Shop:
    _SMALL_SHOP_CAPACITY = 10

    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    def _can_add_item(self):
        return self.items_count < self.capacity - 1

    def _can_remove_item(self, item_name, amount):
        return item_name in self.items \
               and amount <= self.items[item_name]

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, cls._SMALL_SHOP_CAPACITY)

    def add_item(self, item_name):
        if not self._can_add_item():
            return 'Not enough capacity in the shop'
        if item_name not in self.items:
            self.items[item_name] = 0
            self.items_count += 1
        self.items[item_name] += 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name, amount):
        if not self._can_remove_item(item_name, amount):
            return f'Cannot remove {amount} {item_name}'
        self.items[item_name] -= amount
        return f'{amount} {item_name} removed from the shop'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
