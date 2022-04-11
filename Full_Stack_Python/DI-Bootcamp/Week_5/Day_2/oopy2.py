from character import RPG_CHARACTER

class Warrior(RPG_CHARACTER):
    def __init__(self,name, strength, health, stamina, intelligence):
        super().__init__(name, strength, health, stamina, intelligence)
        self.character_class = "Warrior"


conan = Warrior('Conan the Destroyer', 500, 400, 350,20)

conan.walk()
conan.run()
conan.life_bar()

print(conan. character_class)

monster = Monster("Snake", 5 ,5000, 400)
conan.strike(monster)