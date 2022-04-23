total = 0
while True:
    age = input("Please enter your age: ")
    if len(age) == 0:
        break
    elif int(age) <3:
        pass
    elif 3<= int(age) <=12:
        total += 10
    else:
        total += 15
print(f'Your total is {total}')


group = [] 
while True: 
    age = input("Enter age: ") 
    if len(age) == 0: 
        break 
    if 16 <= int(age) <= 21: 
        group.append(int(age)) 
print(group)