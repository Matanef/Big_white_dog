from random import choice

class Game():
    listOfChoise = ['Rock', 'Paper', 'Scissors']

    def get_user_item(self): 
        userInput = input("Please Select one of the following options, Rock, Paper, Scissors: ")
        if userInput in self.listOfChoise:
            return userInput
        else:
            userInput = input("Please Select one of the following options, Rock, Paper, Scissors: ")

        

    def get_computer_item(self):
        computerChoise = []
        randomComputerChoise = choice(self.listOfChoise).lower()
        computerChoise.append(randomComputerChoise)
        print(computerChoise)
        return

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'Draw'
        elif (user_item == 'Rock' and computer_item == 'Scissors') or(user_item == 'Scissors' and computer_item == 'Paper') or (user_item == 'Paper' and computer_item == 'Rock'):
            return 'You Won against the computer'
        else:
            return 'Unfortunatly you lost'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f'you chose {user_item} while the computer selected {computer_item}, and the results (drumrolls) {result}')
        return

selfveriable = Game()
print(selfveriable)
