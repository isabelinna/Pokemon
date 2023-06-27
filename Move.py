import random


class Move:
    def __init__(self, name, move_type, power, accuracy):
        self.name = name
        self.type = move_type
        self.power = power
        self.accuracy = accuracy
    
    def calculate_damage(self):
        attack_damage = self.power * random.uniform(0.85, 1.00)
        return attack_damage
    
    def calculate_multiplier(self, opponent):
        if self.type == "Fire" and opponent.pk_type == "Grass":
            multiplier = 2
        elif self.type == "Water" and opponent.pk_type == "Fire":
            multiplier = 2
        elif self.type == "Grass" and opponent.pk_type == "Water":
            multiplier = 2
        else:
            multiplier = 1
        return multiplier