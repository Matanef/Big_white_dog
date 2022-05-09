import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from random import random

# matrix = np.random.random((3,3))
# print(matrix)

# np.random.randint(4)

# hundredSquare = np.arange(100).reshape(50,2)
# print(hundredSquare)

# firstColumn = hundredSquare.loc[hundredSquare[0]]
# print("Price of each item")
# print(firstColumn)
# print('\n')


arr = np.random.randint(0, 75, (100,))
arr = arr.reshape(50,2)
print(arr.shape)

dataFrame = pd.DataFrame({'x_values': range(1,101), 'y_values': np.random.randn(100)*15+range(1,101) })

fig, ax = plt.subplots(1,2,figsize = (9,9))

ax[0]


xColumn = dataFrame[dataFrame.[0]]
# versicolor_data = data[data.species == 'versicolor']
# virginica_data = data[data.species == 'virginica']

# fig, ax=plt.subplots(1,3,figsize=(13, 5))

# ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
# ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
# ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ax[2].set_ylabel('Frequency')
# ax[0].set_xlabel('petal length (cm)')
# ax[1].set_xlabel('petal length (cm)')
# ax[2].set_xlabel('petal length (cm)')
# plt.show()

# plot

print(xColumn)




