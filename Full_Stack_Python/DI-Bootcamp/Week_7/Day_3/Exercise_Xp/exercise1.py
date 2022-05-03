import matplotlib.pyplot as plt
import pandas as dp
import numpy as np

dataFrame = dp.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print(dataFrame.head(10))

columnsName = list(dataFrame.columns)
print("Column names: ", columnsName)
print('\n')

# Ordinal - Ordinal scale has all its variables in a specific order.
# Nominal is a naming scale, where variables are simply “named” or labeled, with no specific order

# ordinal:
# 1. Pclass
# 2. Sibsp
# 3. Parch (not sure what it means, thirsty?)
# 4. Ticket
# 5. Age
# 6. Fare

# nominal:
#  1. Sex
#  2. Embarked

y = dataFrame['Survived']
x = dp.get_dummies(dataFrame, columns=['Sex', 'Age'])
del x['Survived']
del x['Sex']
del x['Age']

print(x)