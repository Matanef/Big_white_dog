from time import process_time_ns


userNumber = int(input("Please enter a number between 1-100:"))
print(userNumber)
print(type(userNumber))


if userNumber % 3 == 0 and userNumber % 5 == 0:
    print('the number the user entered is devided by three and five with no remaining meaning FizzBuzz {userNumber}')
elif userNumber % 3 == 0:
    print('the number the user entered is devided by three with no remaining meaning Fizz {userNumber}')
elif userNumber % 5 == 0:
    print('the number the user entered is devided by five with no remaining meaning Buzz {userNumber}')
else:
    print('This number is not divided by 3 or 5 with no remaining')