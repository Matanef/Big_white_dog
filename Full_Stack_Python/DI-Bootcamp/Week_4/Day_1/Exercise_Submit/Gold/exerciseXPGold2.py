userMonth = int(input("Please enter a number between 1-12 to represent a month: "))
print(userMonth)
if userMonth >=3 and userMonth <=5:
    print("Spring")
elif userMonth >=6 and userMonth <=8:
    print("Summer")
elif userMonth >=9 and userMonth <=11:
    print("Autumn")
elif userMonth == 12 or userMonth <=2:
    print("Summer")
else:
    print("this is not a vaild number according to the request above")