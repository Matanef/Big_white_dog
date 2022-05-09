import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('titanic')


sns.catplot(x='pclass', data=df, kind='count')  # bar chart
sns.displot(df['age'], kde=False)     
sns.catplot(x='sex', y='age', data=df, kind='box', hue='survived')
sns.catplot(x='sex', y='age', data=df, kind='bar', hue='survived')   
sns.catplot(x='sex', y='age', data=df)   
sns.catplot(x='sex', y='age', data=df, kind='swarm')
sns.catplot(x='sex', y='age', data=df, kind='swarm', hue='survived') 
sns.catplot(x='sex', y='age', data=df, kind='violin', hue='survived')  
sns.catplot(x='sex', y='age', data=df, kind='violin', hue='survived', split=True)   
sns.scatterplot(x='age', y='fare', data=df)    
sns.jointplot(x='age', y='fare', data=df, kind='hex') 


df2 = sns.load_dataset('iris')
df2.head()
sns.pairplot(df2)    # many plots
sns.pairplot(data=df2, hue='species')     # many plots