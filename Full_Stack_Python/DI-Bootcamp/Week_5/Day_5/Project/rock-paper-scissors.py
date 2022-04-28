from game import Game

def get_user_menu_choice():
    # menu = {}
    # menu['1']="Play a New Game." 
    # menu['2']="Show Score."
    # menu['3']="Quite"

    while True: 
        options = menu.keys()
        options.sort()
        for entry in options: 
            print (entry, menu[entry])

        selection=raw_input("Please Select:") 
        if selection =='1': 
            print ("Play") 
        elif selection == '2': 
            print ("Score")
        elif selection == '3': 
            break
        else: 
            print ("Unknown Option Selected!")
        return

def print_results(results):
    wins = len([i for i in results if results[i] == 'win']) 
    draw = len([i for i in results if results[i] == 'draw'])
    losses = len([i for i in results if results[i] == 'loss'])
    print(f"""
Game Results:
You won {wins} times
You lost {losses} times
You got a draw {draw} times
    """)

def main():
    results = {}
    number_of_games = 0
    user_choice = get_user_menu_choice()
    while (user_choice != '3'):
            if user_choice == '1':
                game = Game()
                result = game.play()
                results[number_of_games] = result
                number_of_games += 1
            elif user_choice != '3':
                print("Invalid input, try again")
                user_choice = get_user_menu_choice()
                print(results)
                print_results(results)

main()