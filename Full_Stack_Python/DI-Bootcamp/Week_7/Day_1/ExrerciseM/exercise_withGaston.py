import numpy as np
# Creating the Array
a = np.arange(25).reshape(5,5)
print(a, '\n')

# Extracting diag values from the array and presenting them
print("Performing Diag on array [a] to extract values to a new Array", '\n')
print(np.diagonal(a), '\n')

# crating a new Array of zeros with the diag values we extracted as a diagonal in this array
b = np.diag(np.diagonal(a))
print("Using the array we created with diag values as a diagonal ")
print(b, '\n')

# substracting values of A from B
a = a-b
print(a, '\n')

# creating a new array with the desired values
c= np.diag([1,2,3,4,7])
print("this is c", '\n')
print(c)

# a = a+c
# print(a)



#returnign a line with the diagonal values witch  in turn we can use as an array