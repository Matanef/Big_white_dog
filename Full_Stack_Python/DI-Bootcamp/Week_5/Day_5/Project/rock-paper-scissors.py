def get_user_menu_choice():
    menu = {}
    menu['1']="Play a New Game." 
    menu['2']="Show Score."
    menu['3']="Quite"

    while True: 
        options=menu.keys()
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
    return

def main():
    return