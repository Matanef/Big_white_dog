from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.day)
print(now.hour)
yestrdayAtEightPm = now - timedelta(hours=32)
print(yestrdayAtEightPm)




# print(now)

userBirthDate = input('PLease enter your Birth Date in the following format. DD/MM/YYYY: ')
birthDateInotoInt = datetime.strptime(userBirthDate, '%d/%m/%Y') 

year = int(userBirthDate[-4 :])
print(year)
print(birthDateInotoInt)

month = int(userBirthDate[3:5])
print(month)

daytest = int(userBirthDate[0:2])
print(daytest)




today = datetime.now() 
age = int(today.year - year)
print(today)
print(f"first {age}")

if today.month < month:
    age -= 1

if today.month == month:
    if today.day < daytest:
        age -= 1


print(today)
print(f"second {age}")


ageStr = (str(age))[-1]
print(ageStr)

candles = (int(ageStr) * "i")
print(candles)




long_cake_string = f'''
#       __{candles}__
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
'''
# print(long_cake_string)

if birthDateInotoInt.year % 4 == 0 : 
    if birthDateInotoInt.year % 100 == 0 : 
        if birthDateInotoInt.year % 400 == 0 : 
            print(long_cake_string * 2) 
        else : 
            print(long_cake_string) 
    else : 
        print(long_cake_string * 2) 
else : 
    print(long_cake_string)
