from cmath import sin


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Cat {self.name} is INSTANTIATED!")

    # def __iter__(self):
    #     return self

moshe = Cat("Moshe", 4)
captain_Mittens = Cat("Captain Mittens", 7)
bob = Cat("Bob", 3)

listOfCats = []

listOfCats.append(Cat("Moshe", 4))
listOfCats.append(Cat("Captain Mittens", 7))
listOfCats.append(Cat("Bob", 3))

maxAge = listOfCats[0].age
for singleCat in listOfCats:
        if singleCat.age > maxAge:
            maxAge = singleCat.age
            print(maxAge)
            print(singleCat.name, singleCat.age, sep = ' ')
            print(f"The oldest cat is {singleCat.name}, and is {singleCat.age} years old")
        



