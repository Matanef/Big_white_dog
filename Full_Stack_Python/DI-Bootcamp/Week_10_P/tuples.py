# tuple = ordered and unchangeble

fruits_tuple = ('Apple', 'Mangos', 'Strawberries')

first_fruit = fruits_tuple[0]
print(first_fruit)

fruits_tuple2 = ('apples', )
print(fruits_tuple2)

print(len(fruits_tuple))


# set = unordered and unindexed. No duplicates.
fruits_set = {'Apple', 'Orange', 'Mango'}

print('Apple' in fruits_set)

fruits_set.add('Grape')
print(fruits_set)

fruits_set.clear()
print(fruits_set)