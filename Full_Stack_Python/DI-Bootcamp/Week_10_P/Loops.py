people = ['Matan', 'Camila', 'Rafa']

# for Loop
for person in people:
    print(person, 'is in the list')

print('===================================')

for person in people:
    print(person, 'is in the list')
    if person == 'Matan':
        break


print('===================================')

for person in people:
    if person == 'Camila':
        continue
    print(person, 'is in the list')

print('===================================')

for i in range(len(people)):
    print(people[i], 'is cool')

print('===================================')

for i in range(0, 10):
    print(i)

print('===================================')

count = 0
while count <= 10:
    print('Count :', count)
    count +=1