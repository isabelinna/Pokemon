#Pokemon-inspired 1v1 game 🐉
#Author Isabel Vieyra 

from Pokemon import Pokemon
from Move import Move
from Trainer import Trainer


pokemon1 = Pokemon("Charizard", 50, 100, "Fire")
pokemon2 = Pokemon("Blastoise", 55, 120, "Water") 
pokemon3 = Pokemon("Venusaur", 60, 110, "Grass")
pokemon4 = Pokemon("Arcanine", 48, 95, "Fire")
pokemon5 = Pokemon("Lapras", 52, 130, "Water")
pokemon6 = Pokemon("Exeggutor", 45, 90, "Grass")
pokemon7 = Pokemon("Ninetales", 42, 85, "Fire")
pokemon8 = Pokemon("Gyarados", 47, 115, "Water")
pokemon9 = Pokemon("Tangrowth", 40, 80, "Grass")
pokemon10 = Pokemon("Typhlosion", 50, 100, "Fire")

# Fire type moves
fire_move1 = Move("Flamethrower", "Fire", 80, 0.90)
fire_move2 = Move("Fire Blast", "Fire", 110, 0.85)
fire_move3 = Move("Fire Punch", "Fire", 75, 0.95)
fire_move4 = Move("Flare Blitz", "Fire", 120, 0.80)

# Water type moves
water_move1 = Move("Water Gun", "Water", 40, 1.00)
water_move2 = Move("Hydro Pump", "Water", 110, 0.80)
water_move3 = Move("Surf", "Water", 90, 0.95)
water_move4 = Move("Aqua Tail", "Water", 80, 0.90)

# Grass type moves
grass_move1 = Move("Razor Leaf", "Grass", 55, 0.95)
grass_move2 = Move("Solar Beam", "Grass", 120, 0.75)
grass_move3 = Move("Seed Bomb", "Grass", 80, 0.90)
grass_move4 = Move("Leaf Blade", "Grass", 90, 0.95)

pokemon1.moves = [fire_move1, fire_move3]
pokemon2.moves = [water_move2, water_move3, water_move4]
pokemon3.moves = [grass_move3, grass_move4]
pokemon4.moves = [fire_move3, fire_move4]
pokemon5.moves = [water_move1, water_move2, water_move3 ]
pokemon6.moves = [grass_move1, grass_move2]
pokemon7.moves = [fire_move1, fire_move2, fire_move3, fire_move4]
pokemon8.moves = [water_move1, water_move4]
pokemon9.moves = [grass_move2, grass_move3, grass_move4]
pokemon10.moves = [fire_move2, fire_move3, fire_move4]

pokemons = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10]
actions = ["Attack", "Heal", "Switch", "Give Up"]
game_over = False
def handle_turn(trainer, opponent):
    
    print("{trainer_name}´s active Pokémon: {active_pokemon.name} (HP: {active_pokemon.hp})".format(trainer_name = trainer.name, active_pokemon=trainer.active_pk))
    [print(action) for action in actions]
    choice = int(input("What will you do? "))
    
    if choice == 0:
        # Attack
        if opponent.active_pk is None:
            print("Opponent has no Pokémon out. Switch to a Pokémon first.")
        else:
            print("Moves:")
            for index, move in enumerate(trainer.active_pk.moves):
                print("{index}: {move_name}".format(index=index, move_name=move.name))
            
            move_selection = int(input("Select a move (enter move index): "))
            trainer.attack(trainer.active_pk, opponent.active_pk, trainer.active_pk.moves[move_selection])
    elif choice == 1:
        # Heal
        trainer.heal(trainer.active_pk)
    elif choice == 2:
        # Switch
        trainer.switch(trainer.pokemon_team)
    
    elif choice == 3:
        # Give up
        trainer.give_up()
        return True
    
    if opponent.active_pk is not None and opponent.active_pk.hp <= 0:
        print("{trainer_name} wins!".format(trainer_name=trainer.name))
        return True
    
    return False

# Game start
print("Welcome, Trainers!")
trainer1_name = input("Trainer 1, enter your name: ")
trainer2_name = input("Trainer 2, enter your name: ")

trainer1 = Trainer(trainer1_name)
trainer2 = Trainer(trainer2_name)

# Select Pokémon
trainer1.select_team(pokemons)
trainer2.select_team(pokemons)

print("{trainer_name}, it's your turn!".format(trainer_name=trainer1.name))
print("Which pokemon will you send out?")
for index, pokemon in enumerate(trainer1.pokemon_team):
            print("{index}: {name} ({pk_type})".format(index=index, name=pokemon.name, pk_type=pokemon.pk_type))

active = int(input("Enter the index of your chosen Pokémon: "))
if active >= 0 and active < len(trainer1.pokemon_team):
    trainer1.active_pk = trainer1.pokemon_team[active]

print("{trainer_name}, it's your turn!".format(trainer_name=trainer2.name))
print("Which pokemon will you send out?")
for index, pokemon in enumerate(trainer2.pokemon_team):
    print("{index}: {name} ({pk_type})".format(index=index, name=pokemon.name, pk_type=pokemon.pk_type))
active = int(input("Enter the index of your chosen Pokémon: "))
if active >= 0 and active < len(trainer2.pokemon_team):
    trainer2.active_pk = trainer2.pokemon_team[active]

while not game_over:
    if handle_turn(trainer1, trainer2):
        game_over = True
    
    if not game_over and handle_turn(trainer2, trainer1):
        game_over = True