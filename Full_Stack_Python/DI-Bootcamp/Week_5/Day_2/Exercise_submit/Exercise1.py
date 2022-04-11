class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Cat {self.name} is INSTANTIATED!")

    def walk(self):
        return f'{self.name} is just walking around'

    def __repr__(self):
        return f'{self.name} are Walking!!!'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Kinkalow(Cat):
    def sing(self, sounds):
        return f'{sounds}'



moshe = Cat("Moshe", 2)
captain_Mittens = Cat("Captain Mittens", 6)
bob = Cat("Bob", 4)

my_cats = []

my_cats.append(Cat("Moshe", 2))
my_cats.append(captain_Mittens)
my_cats.append(bob)

my_pets = my_cats

print(my_pets)
print(my_cats[0])