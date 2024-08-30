import numpy as np

# # Numpy Practice
# a = np.array([1,2,3], dtype='int16')
# print(a)

# b = np.array([[7.0,8.0,10.0],[5.0,2.0,11.0]])
# print(b) 

# # Get Dimension
# print(a.ndim)
# print(b.ndim)

# # Get Shape / Kinda like the len function in py 
# print(a.shape)
# print(b.shape)

# # Get Type
# print(a.dtype)
# print(b.dtype)

# # Get Size
# print(a.itemsize)
# print(b.itemsize)

# # Get total size
# print(a.nbytes)
# # Or
# a.size

# Range
np1 = np.arange(10)
print(np1)

# Step
np2 = np.arange(0, 10, 2)
print(np2)

np3 = np.zeros(10)
print(np3)

# Multidimensional zeros
np4 = np.zeros((2,10))
print(np4)

# Full
np5 = np.full((10), 6)
print(np5)

# Multidimensional Full
np6 = np.full((2,10), 6)
print(np6)
 
# Accessing/Changing specific elements, rows, columns

# Getting a specifc element
c = np.array([[8, 6, 8],[5, 9, 2]])
print(c[1,2])

# Getting a specific row
print(c[1, :])

# Getting a specific column
print(c[:, 0])

# Convert Python lists to np

my_list = [1,2,3,4,5]
np7 = np.array(my_list)
print(np7)
