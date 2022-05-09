import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
cars_df = pd.read_csv(url).dropna(subset=['Manufacturer', 'Price'])

means = cars_df[['Manufacturer', 'Price']].groupby('Manufacturer').mean()
cars_df['Manufacturer_transformed'] = cars_df['Manufacturer'].dropna().apply(lambda x: means.loc[x, "Price"])
cars_df[['Manufacturer', 'Manufacturer_transformed', 'Price']].head()

print(cars_df)



make_column = cars_df.Make
print(make_column.head(3))

make_dict = {v: k for k,v in enumerate(make_column)}
encoded_make = make_column.map(lambda x: make_dict[x])
