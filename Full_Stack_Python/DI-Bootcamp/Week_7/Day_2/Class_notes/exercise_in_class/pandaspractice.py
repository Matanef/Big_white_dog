import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(df.head(5))
print('\n')
blah = df.iloc[50,60:2]
print(blah)
print('\n')
blahTwo = df[['species', 'petal_length', 'petal_width']]
print(blahTwo)

blahGroupmean = df.groupby('species').apply(np.mean)
blahGroupSum = df.groupby('species').apply(np.sum)
print("Mean value:", blahGroupmean)