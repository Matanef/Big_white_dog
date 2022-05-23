import json

from matplotlib.style import use

userJson = '{"first_name": "Matan", "last_name": "Efrati", "age": "37"}'

user = json.loads(userJson)
print(user)
print(user['first_name'])

# dump to create Json
car = {
    'Brand': 'Kia',
    'Model': 'Sportage',
    'year': '2016',
}

carjson = json.dumps(car)
print(carjson)

