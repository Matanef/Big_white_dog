import matplotlib.pyplot as plt #conventional syntax 
import numpy as np
import pandas as pd


# x = [1,2,3,4]
# y = [2, 20, 35, 6]

# plt.plot(x, y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('first graph')
# plt.show()

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

plt.plot(data["sepal_length"], "r--") 
plt.show()

plt.scatter(data['sepal_length'], data['petal_length'])
plt.xlabel('sepal_length (cm)')
plt.ylabel('petal_length (cm)')
plt.grid() 

plt.plot(data["sepal_length"], data["sepal_width"] , 'bo')
# plt.show()

setosa_data = data[data.species == 'setosa']
versicolor_data = data[data.species == 'versicolor']
virginica_data = data[data.species == 'virginica']

fig, ax=plt.subplots(1,3,figsize=(13, 5))

ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[0].set_ylabel('Frequency')
ax[1].set_ylabel('Frequency')
ax[2].set_ylabel('Frequency')
ax[0].set_xlabel('petal length (cm)')
ax[1].set_xlabel('petal length (cm)')
ax[2].set_xlabel('petal length (cm)')
plt.show()