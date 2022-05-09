import numpy as np
import pandas as pd
import random

# 1. Write a function to create a numpy array using only the input: start, length, and stop.
# Use the function to create an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers
firstarray = np.arange(6,100,4)
print(firstarray)

# def Create_array(start, length, step):
#     return np.array()

# arrayFromFunc = Create_array(6, 100, 4)

#  2. Drop all nan values from the following numpy array. 

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
a = a[~np.isnan(a)]
print(np.isnan(a))
print(a)


# 
# print(a)

# random_numpy_array = np.array([random.randint(1,100) for _ in range(5 * 6)]).reshape((5,6))

# for row in random_numpy_array:
#     print(np.max(row))