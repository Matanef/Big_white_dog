myfile = open('myfile.txt', 'w')

# print('Name: ', myfile.name)
# print('Is Closed: ', myfile.closed)
# print('Mode: ', myfile.mode) 

# myfile.write('Hello All, I Love Python')
# myfile.write(' and Breakfast')
# myfile.close()


loremText = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''



# Append
myfile = open('myfile.txt', 'w')
myfile.write(' i also like some other langs')
for i in range(50):
    myfile.write(loremText)
myfile.close()

# Read
myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
text = myfile.readlines(100)
print(text)
myfile.close()