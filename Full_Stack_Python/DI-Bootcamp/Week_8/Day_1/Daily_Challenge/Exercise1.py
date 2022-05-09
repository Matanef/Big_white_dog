import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gapminder import gapminder


df = sns.load_dataset('titanic')


sns.catplot(x='pclass', data=df, kind='count')  # bar chart
sns.displot(df['age'], kde=False)     
sns.catplot(x='sex', y='age', data=df, kind='box', hue='survived')
sns.catplot(x='sex', y='age', data=df, kind='bar', hue='survived')   
sns.catplot(x='sex', y='age', data=df, kind='violin', hue='survived')  
sns.catplot(x='sex', y='age', data=df, kind='violin', hue='survived', split=True)   
sns.catplot(x='embark_town', y='age', data=df, kind='swarm', hue='survived', height=12) 


plt.show()

