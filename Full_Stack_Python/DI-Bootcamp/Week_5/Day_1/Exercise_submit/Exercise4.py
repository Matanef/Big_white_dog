from itertools import count


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.sorted_animals = {}

    def add_animal(self, new_animal):
        if self.animals.count(new_animal) ==0:
            self.animals.append(new_animal)



    def get_animals(self):
        for animals in self.animals:
            print(animal)

    def sell_animals(self, animal_sold):
        if self.animals.count(animal_sold) ==0:
            self.animals.remove(animal_sold)

    def sort_animal(self):
        