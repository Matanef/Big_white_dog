import numpy as np
import pandas as pd

chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')


chipoInfo = chipo.info
print(chipoInfo)
print('\n')
chipoDescribe = chipo.describe
print(chipoDescribe)
print('\n')
firstTen = chipo.head(10)
print(firstTen)
print('\n')
chipoShape = chipo.shape
print(chipoShape, 'According to .shape we have 4622 observations and 5 columns')
print('\n')


