import random

class Trainer:
    def __init__(self,name):
        self.name = name
        self.active_pk = []
        self.pokemon_team = []
    
    def attack(self, pokemon, opponent, move):
        print("Trainer {name} attacked with {pokemon.name}".format(name=self.name, pokemon=pokemon))
        print("{pokemon.name} used {move.name}".format(pokemon=pokemon, move=move))
        damage = round(move.calculate_damage(),0)
        type_multiplier = move.calculate_multiplier(opponent)
        if type_multiplier == 2:
            print("It's super effective!")
        print("{opponent.name} lost {damage} health points.".format(opponent=opponent, damage=damage))
        opponent.hp -= damage
        if opponent.hp <= 0:
            print("{opponent.name} fainted!".format(opponent=opponent))
    
    def heal(self, pokemon):
        print("Trainer {name} healed {pokemon.name}".format(name=self.name, pokemon=pokemon))
        healed_amount = int(pokemon.hp * random.uniform(0.2, 0.4))
        print("{pokemon.name} gained {healed_amount} health points!".format(pokemon=pokemon, healed_amount=healed_amount))
        pokemon.hp += healed_amount
    
     
    def give_up(self, opponent):
        print("Oh noes! {trainer_name} ran away from battle...".format(trainer_name = self.name))
        print("{opponent_name} wins!".format(opponent_name = opponent.name))

    def switch(self, pokemon_team):
        print("Which Pokémon will you send out?")
        for index, pokemon in enumerate(pokemon_team):
            print("{index}: {pokemon.name} ({pokemon.pk_type})".format(index=index, pokemon=pokemon))
    
        
        while True:
            try:
                selection = int(input("Enter the index of the Pokémon you want to switch to: "))
                if selection >= 0 and selection < len(pokemon_team):
                    new_active_pk = pokemon_team[selection]
                    if new_active_pk.hp > 0:
                        print("You sent out {new_active_pk.name}!".format(new_active_pk=new_active_pk))
                        self.active_pk = new_active_pk
                        break
                    else:
                        print("That Pokémon has fainted. Please choose another.")
                else:
                    print("Invalid index. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        
    def select_team(self,pokemons):
        print("Trainer {name}, select your team of 6 Pokémon.".format(name=self.name))
        remaining_pokemons = pokemons.copy()
        
        for _ in range(6):
            print("Choose a Pokémon by entering its index:")
            for index, pokemon in enumerate(remaining_pokemons):
                print("{index}: {name} ({pk_type})".format(index=index, name=pokemon.name, pk_type=pokemon.pk_type))
            
            while True:
                try:
                    selection = int(input("Enter the index of your chosen Pokémon: "))
                    if selection >= 0 and selection < len(remaining_pokemons):
                        chosen_pokemon = remaining_pokemons.pop(selection)
                        self.pokemon_team.append(chosen_pokemon)
                        break
                    else:
                        print("Invalid index. Please choose again.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")