class PizzaDelivery:
    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_ingredient * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_ingredient * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

        if ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_ingredient

    def make_order(self):
        temp = []
        self.ordered = True
        for k, v in self.ingredients.items():
            if k == list(self.ingredients)[-1]:
                temp.append(f'{k}: {v}')
                break
            temp.append(f'{k}: {v}', )
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join([x for x in temp])}' \
               f' and the price will be {self.price}lv.'


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
