import numpy as np

def calculate_arr(one_dim_arr):
    minElement = np.amin(one_dim_arr)
    stdElement = np.std(one_dim_arr)
    prodElement = np.prod(one_dim_arr)
    proddElemet = np.dot(one_dim_arr, one_dim_arr)

    return minElement, stdElement, proddElemet,proddElemet
    
array = np.arange(10)
print(array)
array_min, array_std, array_prod, array_dProd = calculate_arr(array)

print(array_min, array_std, array_prod, array_dProd)

# one_dimension = np.array([1,2,3,4])
# print(one_dimension[:])

# minElement = np.amin(one_dimension)
# print(minElement)

# stdElement = np.std(one_dimension)
# print(stdElement)

# prodElement = np.prod(one_dimension)
# print(minElement)

# proddElemet = np.dot(one_dimension, one_dimension)
# print(proddElemet)