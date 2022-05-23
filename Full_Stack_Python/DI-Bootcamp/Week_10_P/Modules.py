import datetime
from datetime import date
import sys
import time
from validators import validate_email


today = date.today()
print(today)
timestamp = time.time()
print(timestamp, today)


email = 'matanefrati@gmail.com'

if validate_email(email):
    print('the email is Valid')
else:
    print('email not Valid')