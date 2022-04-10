toppings = [] 
 
while True: 
    pizza = input("input pizza topping, when finshed write quit: ") 
    if pizza != "quit": 
        print(f"i'll add that ({pizza}) to the pizza") 
        toppings.append(pizza) 
    else: 
        total = 10 + (2.5*len(toppings)) 
        print(f"You're toppings are {toppings}, and you're total fee is {total}") 
        break