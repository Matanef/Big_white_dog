import numpy as np
import pandas as pd

chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')



chipoDescribe = chipo.describe
print(chipoDescribe)
print('\n')
firstTen = chipo.head(10)
print(firstTen)
print('\n')

chipoShape = chipo.shape
print(chipoShape, 'According to .shape we have 4621 observations (amount 4621 -1 for the column names) and 5 columns')
print('\n')

columnsName = list(chipo.columns)
print("Column names: ", columnsName)
print('\n')

columnNumber = chipo.shape[1]
print("Column numbers: ", columnNumber)
print('\n')

chipoInfo = chipo.info
print("Some .Info")
print(chipoInfo)
print('\n')


# i didn't understand the question of how the database is indexed, does it mean when i first look at it with out filtering?
# if yes then it would probably be by description (to group them together to categories) and then inside each category by name
# i just read about indexing in pandas and it's only describing indexing, giving numbers or selecting by numbers so i don't understand the question.

# for question 9 i didn't understand it aswell so what i'm trying to do is to see which item in the order_id appears the most and get it's name.
chipoMostOrder = chipo['order_id'].mode()
print(chipoMostOrder)
chipoOrderLoc = chipo.loc[chipo['order_id'] == 926]
print(chipoOrderLoc)

# hope this is ok



