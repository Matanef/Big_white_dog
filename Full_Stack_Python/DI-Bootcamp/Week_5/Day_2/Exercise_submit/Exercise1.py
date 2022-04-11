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
        return f'{self.name} is Walking!!!'

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
print(my_cats)

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print(f'{self.name} has been INSTANTIATED')
    
    def bark(self):
        return f'{self.name} is Barking'

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        if self.run_speed() < other_dog.run_speed():
            return f'{other_dog.name} wins'
        else: 
            return f'{self.name} wins'


lanou = Dog("Lanou", 8, 35)
dov = Dog("Dov", 10, 53)
katzie = Dog("Katzie", 12 , 16)

listOfDogs = []

listOfDogs.append(lanou)
listOfDogs.append(dov)
listOfDogs.append(katzie)

print(lanou.fight(katzie))

