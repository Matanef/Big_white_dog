import numpy as np
import pandas as pd

chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')

chipo["item_price"] = chipo["item_price"].str.replace("$", "").astype("float64")
biggerThenTen = chipo[chipo["item_price"] > 10.00]["item_price"].count()
print(biggerThenTen)
print('\n')

price = chipo[["item_name", "item_price"]]
print("Price of each item")
print(price)
print('\n')

sortName = price.sort_values(by="item_name")
print("Sorted by Name")
print(sortName)
print('\n')

quantityOfExpensive = chipo.sort_values(by="item_price", ascending=False)["quantity"].iloc[0]
print("Quantity of the most expensive item ordered")
print(quantityOfExpensive)
print('\n')
