

fruitsInput = input('Please enter your FAVORITE fruits, in addition please seperate the input with the space bar: ').split(" ")
# print(fruitsInput)
# fruits = fruitsInput.split(" ")
# print(fruits)

fruitNew = input('Now Select any Fruit...')

# for fruitNew in fruits:
if fruitNew in fruitsInput:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')
