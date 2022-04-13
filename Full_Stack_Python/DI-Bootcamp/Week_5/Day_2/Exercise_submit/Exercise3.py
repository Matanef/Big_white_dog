from Exercise1 import Dog
from random import randint

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        args = list(args)
        # dogPlay = " ".join(args)
        return f'{self} and {args} play togather'
        # for i in args:
            # if i < len(list):
            #     i += 1
            #     print(f'{self},{args} are all play together')
            # print(dogPlay)
    
    def __repr__(self):
        return f'{self.name}'

    def do_a_trick(self):
        sentence = [f"{self.name} does a barrel roll.", f"{self.name} stands on his back legs.", f"{self.name} shakes your hand.", f"{self.name} plays dead."]
        if self.trained:
           return (sentence[randint(0,len(sentence)-1)])

lanou = PetDog("Lanou", 8, 35)
dov = PetDog("Dov", 10, 53)
katzie = PetDog("Katzie", 12 , 16)

# katzie.train()
# katzie.do_a_trick()

print(katzie.play(dov))
print(katzie.train())
print(katzie.do_a_trick())




