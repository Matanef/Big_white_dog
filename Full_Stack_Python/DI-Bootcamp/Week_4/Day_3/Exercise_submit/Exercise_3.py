
store = {
    'name': 'Zara',
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': 7000,
    'major_color': { 
        'France': 'blue', 
        'Spain': 'red', 
        'US': {'pink', 'green'}
    }
}

store['number_stores'] = 2
print(store)

print('the customers of Zara are ' + ", ".join(str(i) for i in store['type_of_clothes'][0:3]) )
store['country_creation'] = 'Spain'
if 'international_competitors' in store:
	    store['international_competitors'].append("Desigual")
print(store)
print()
print()
del store['creation_date']
print(store)


print(store['international_competitors'][-1])
print()
print()
print("The major colors in the US are : " + ", ".join(store['major_color']['US']) )

print()
print()
print(len(store))
print()
print()
print(store.values())

print()
print()
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
store.update(more_on_zara)
print(store)

