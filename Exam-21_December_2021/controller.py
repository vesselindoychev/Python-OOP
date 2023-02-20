from project import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []
        self.player_names = set()

    def __food_sustenance(self):
        food = [x for x in self.supplies if x.__class__ == Food]
        return food

    def __drink_sustenance(self):
        drink = [x for x in self.supplies if x.__class__ == Drink]
        return drink

    def __search_player_by_name(self, player_name):
        for x in self.players:
            if player_name == x.name:
                return x

    def add_player(self, *args: Player):
        current_players = []
        for player in args:
            if player.name not in self.player_names:
                self.player_names.add(player.name)
                self.players.append(player)
                current_players.append(player.name)
        return f"Successfully added: {', '.join(current_players)}"

    def add_supply(self, *args: Supply):
        for x in args:
            self.supplies.append(x)

    def sustain(self, player_name, sustenance_type):
        food_sustenance = self.__food_sustenance()
        drink_sustenance = self.__drink_sustenance()
        player = self.__search_player_by_name(player_name)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type == 'Food':
            if len(food_sustenance) == 0:
                raise Exception(f"There are no food supplies left!")
            last_food_supply = food_sustenance[-1]
            if player.stamina + last_food_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += last_food_supply.energy
            food_sustenance.remove(last_food_supply)
            self.supplies.remove(last_food_supply)
            return f"{player_name} sustained successfully with {last_food_supply.name}."

        if sustenance_type == 'Drink':
            if len(drink_sustenance) == 0:
                raise Exception("There are no drink supplies left!")
            last_drink_supply = drink_sustenance[-1]

            if player.stamina + last_drink_supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += last_drink_supply.energy
            drink_sustenance.remove(last_drink_supply)
            self.supplies.remove(last_drink_supply)
            return f"{player_name} sustained successfully with {last_drink_supply.name}."

    def duel(self, first_player_name, second_player_name):
        result = ''
        first_player = self.__search_player_by_name(first_player_name)
        second_player = self.__search_player_by_name(second_player_name)
        for x in [first_player, second_player]:
            if x.stamina == 0:
                result += f'Player {x.name} does not have enough stamina.\n'
        if result:
            return result

        if first_player.stamina < second_player.stamina:
            if second_player.stamina - first_player.stamina / 2 <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            second_player.stamina -= first_player.stamina / 2
        elif second_player.stamina < first_player.stamina:
            if first_player.stamina - second_player.stamina / 2 <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            first_player.stamina -= second_player.stamina / 2

        return f"Winner: {first_player.name}" if first_player.stamina > second_player.stamina else \
            f"Winner: {second_player.name}"

    def next_day(self):
        food = self.__food_sustenance()
        drink = self.__drink_sustenance()

        for player in self.players:
            if player.stamina - player.age * 2 <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')
