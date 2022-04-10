from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.day)
print(now.hour)
yestrdayAtEightPm = now - timedelta(hours=32)
print(yestrdayAtEightPm)







# print(now)

userBirthDate = input('PLease enter your Birth Date in the following format. DD/MM/YYYY: ')
print(userBirthDate)
birthDateInotoInt = datetime.strptime(userBirthDate, '%d/%m/%Y') 
print(birthDateInotoInt)
today = datetime.now() 
age = int(today - birthDateInotoInt)
print(age)

# enough it's four oclock and i need to sleep






#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~