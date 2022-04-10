


class Farm:
# 1. yes, the farm class should have an __init__ method to reference to and it takes the self parameter and the name which is the animal name in the farm. 
# 2. currently as i'm writing this i think it should be 
    def __init__(self, name):
        self.name= name
        self.animals = []

    def add_animal(self, name, amount):
        if name in self.animals:
            animalName = self.animals[self]
            # print(animalName)
            self.animals.append({name: animalName + amount})
        else:
            self.animals[name]= amount
            



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

