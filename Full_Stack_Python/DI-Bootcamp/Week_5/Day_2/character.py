from email.base64mime import header_length
from queue import LifoQueue


class RPG_CHARACTER():
    def __init__(self, name, strength, health, stamina, intelligence):
        self.name = name
        self.strength = strength
        self.stamina = stamina
        self.intelligence = intelligence
        self.is_dead = False
        self.character_class = "Warrior"
        self.health = health
        self.level = 0
        print(f"RPG CHARACTER {self.name} INSTANTIATED!")
    
    def __repr__(self):
        return f"{self.name}'s' stats:\nlevel: {self.level}\nstrength: {self.strength}\nstamina: {self.stamina}\nintelligenct: {self.intelligence}\nclass: {self.character_class}"
    def walk(self):
        print(f"{self.name} is walking...")
    def jump(self):
        print(f"{self.name} is jumping...")
    def run(self):
        print(f"{self.name} is running...")
    def strike(self, monster):
        print(f"{self.name} is striking {monster.name}")
        monster.health -= self.strength
    def life_bar(self):
        if self.health < 0:
            self.is_dead = True
        print(f"{self.name}'s health: {self.health}")
joe = RPG_CHARACTER("Joe", 100, 200, 75, 20)
zina = RPG_CHARACTER("Zina", 120, 300, 150, 100)
print(joe)
print()
print(zina)
print()
# zina.walk()
print(zina.level)




class Monster():
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.is_dead = False
    def strike(self, hero):
        print(f"{self.name} is striking {hero.name}")
        hero.health -= self.strength
        
    def life_bar(self):
        if self.health < 0:
            self.is_dead = True
        print(f"{self.name}'s health: {self.health}")
monster = Monster("Kraken", 2, 50, 4)
monster.strike(zina)
zina.life_bar()
zina.strike(monster)
monster.life_bar()

while zina.walk:
    # print(zina.walk())
    if zina.life_bar == 300:
        print(zina.walk)
    elif zina.life_bar == 290:
        print(zina.run)
    else:
        break