import numpy as np
import pandas as pd

user_df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', delimiter = '|')

print(user_df.head(5))

user_df_mean = user_df[['occupation', 'age']].groupby(by = 'occupation').apply(np.mean)
print(user_df_mean)

male = user_df.loc[user_df['gender'] == 'M']
print(male)
total_occupation = user_df.groupby(['occupation']).count().iloc[:1]
print(total_occupation)

number_male_occupation = male.groupby(['occupation']).count().iloc[:1]

# calc = (number_male_occupation / total_occupation).sort_values()

minAge = user_df[['occupation', 'age']].groupby('occupation').min()
print(minAge)

