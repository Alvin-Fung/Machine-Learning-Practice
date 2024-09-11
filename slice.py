import numpy as np

# Slicing Numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2, 3, 4, 5
print(np1[1:5])

# Return from something till the end of the array?
# 4 - 9
print(np1[3:])

# Return Negative Slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5]) # 2 - 5
print(np1[1:5:2]) # 2- 5  in steps of 2

# Steps on the entire array
print(np1[::2])
print(np1[::3])

# Slice a 2-d array
np2 = np.array([
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10]])
# Pull out a single item from the array
print(np2[1,2])

# Slice a 2-d array
print(np2[0:1, 1:3]) # 1st element is the 1st list until, but not including, the 2nd list. 2nd element is the slice 
