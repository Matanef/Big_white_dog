from Exercise1 import Dog

class PetDog(Dog):
    def __init__(self, trained):
        self.trained = False

    def train(self):
        print(self.bark)
        self.trained = True
    
    def play(self, *args):
        print(f'{args.name} all play together')





