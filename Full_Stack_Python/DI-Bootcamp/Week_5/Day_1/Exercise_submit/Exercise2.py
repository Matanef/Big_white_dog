class Dog:
    def __init__(self, name ,height):
        self.name = name
        self.height = height
        # print(f"The Dog {self.name} is INSTANTIATED!")
        print()
        print(f"Dog Details:\nName: {self.name}\nHeight: {self.height}")

    def bark(self):
        print (f"{self.name} goes Woof!")

    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high!")

    
lanou = Dog("Lanou", 35)
dov = Dog("Dov", 53)
katzie = Dog("Katzie", 16)
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)


# Lanou = Dog("Lanou", 35)
lanou.bark()
lanou.jump()
dov.jump()

print()
davids_dog.bark()
davids_dog.jump()
print()

sarahs_dog.bark()
sarahs_dog.jump()

print()
print()
print()
listOfDogs = []

listOfDogs.append(Dog("Lanou", 35))
listOfDogs.append(Dog("Dov", 53))
listOfDogs.append(Dog("Katzie", 16))
listOfDogs.append(Dog("Rex", 50))
listOfDogs.append(Dog("Teacup", 20))

maxHeight = listOfDogs[0].height
for singleDog in listOfDogs:
        if singleDog.height > maxHeight:
            maxHeight = singleDog.height
            print()
            print()
            print(maxHeight)
            print(singleDog.name, singleDog.height, sep = ' ')
            print(f"The Biggest Boi is {singleDog.name}, and is {singleDog.height} cm high")



