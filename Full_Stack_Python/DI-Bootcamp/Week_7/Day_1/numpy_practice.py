import numpy as np

lst = [1,2,3]
lst_array = np.array(lst)

print('Regular List: ', lst)
print('Numpy array: ', lst_array)

print(lst_array[0])
print(lst_array[-1])

lst_2nd = [[3,5,7,-4,1], [0,5,33,-750,2], [4,4,4,4,3]]
print(lst_2nd)
lst_2nd_arr = np.array(lst_2nd)
# The Shape of the Array
print(lst_2nd_arr.shape)
print(lst_2nd_arr, '\n')

# The Reshape of the Array
lst_2nd_arr = lst_2nd_arr.reshape((-1,3))
print(lst_2nd_arr, '\n')
print(lst_2nd_arr.shape)

# Flattening into 1-d
lst_2nd_arr = lst_2nd_arr.reshape((15,))
lst_2nd_arr = np.array(lst_2nd)
print(lst_2nd_arr, '\n')
print(lst_2nd_arr.shape)

# # 1-d
# []
# # 2-d
# [[],[]]
# # 3-d
# [[],[],[]]

one_dimension = np.array([1,2,3,4])
print(one_dimension[:])

two_dimension = np.array([[1,2,3,4], [5,6,7,8]])
print('line 41', two_dimension[:])
# specific column and index
print('line 43',two_dimension[1,1])
# All values from specific column
print('line 45',two_dimension[:,1])
# All values from specific row
print('line 47',two_dimension[1,:])


arr = np.array([1,2,3,4,5,6,7,8,9,10])
print('line 51',arr.reshape(-1, 2))
arr = arr.reshape((-1, 2))

arr2 = np.array([[1,2,3,4],[1,2,3,4]])
# np.dot/np.matmul for multiplication
np.dot(arr,arr2)

print('line 58',arr - 1)

#create numpy array from range + reshape
range_array = print('line 61', np.arange(16).reshape((4,4)))



# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr.reshape(-1,2))

# arr2 = np.array([[1,2,3,4],[1,2,3,4]])

