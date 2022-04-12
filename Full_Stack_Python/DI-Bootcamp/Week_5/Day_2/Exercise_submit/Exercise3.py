from Exercise1 import Dog
from random import randint

class PetDog(Dog):
    def __init__(self, trained):
        self.trained = False

    def train(self):
        print(self.bark)
        self.trained = True
    
    def play(self, *args):
        print(f'{args.name} all play together')

    def do_a_trick():
        sentence = [f"{self.name} does a barrel roll.", f"{self.name}] stands on his back legs.", f"{self.name} shakes your hand.", f"{self.name} plays dead."]
        while self.trained == True:
            print(sentence[randint(0,len(sentence)-1)])

lanou = Dog("Lanou", 8, 35)
print(lanou.play())




