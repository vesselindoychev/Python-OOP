from demo_project.customer import Pokemon
from demo_project.exercise_plan import Trainer

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
third_pokemon = Pokemon("Bolbasor", 290)

print(trainer.add_pokemon(third_pokemon))

print(trainer.trainer_data())
