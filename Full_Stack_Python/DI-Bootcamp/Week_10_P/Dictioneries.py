person = {
    # key: value
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
}

# get Value
print(person)
print(person['first_name'])

# add key/vlaue
person['phone'] = '0559999999'
print(person)
print(person['phone'])

# get Key or Value
print(person.keys())
print(person.values())

# make a copy
person2 = person.copy()
person2['city'] = 'Tel Aviv'
print(person2['city'])

del(person2['age'])
person2.pop('phone')

print(person2)


people = [
    {'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,},
    {'first_name': 'Dani',
    'last_name': 'Odon',
    'age': 26,}
]

print(people[0])
print(people[1]['first_name'])
print(person2)
print(person)