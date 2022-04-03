userHeight = float(input("please enter your height in inches: "))
formula = userHeight*2.54
print(formula)


if formula > 145:
    print("You are High Enough to ride the Roller Coster")
else:
    print("You are not High enough to ride the Coster, try again next year")
