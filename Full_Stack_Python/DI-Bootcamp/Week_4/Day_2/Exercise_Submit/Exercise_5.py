basket = ['Banana', 'Apples', 'Oranges', 'Blueberries']
print(basket.index('Apples'))
basket.remove('Banana')
print(basket)

basket.remove('Blueberries')
print(basket)

basket.append('Kiwi')
print(basket)

basket.insert(0, 'Apples')
print(basket)

print(basket.count('Apples'))

basket.clear()
print(basket)

