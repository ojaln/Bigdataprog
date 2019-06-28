# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:05:33 2019

@author: ADMIN
"""

# Exercise 1: Replace all odd numbers in arr with -1
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
arr

# Exercise 2: Convert a 1D array to a 2D array with 2 rows
arr = np.arange(10)
arr.reshape(2, -1) 

# Exercise 3: Create the following pattern without hardcoding
a = np.array([1,2,3])
np.r_[np.repeat(a, 3), np.tile(a, 3)]

# Exercise 4: Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

# Exercise 5: Get the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)

# Exercise 6: Create a 2D array of shape 5x3 to contain random decimals between 5 and 10.
arr = np.arange(9).reshape(3,3)
rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
print(rand_arr)

# Exercise 7: Limit no of items printed in python numpy array a to a max of 6.
np.set_printoptions(threshold=6)
a = np.arange(15)
a

# Exercise 8: Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.set_printoptions(suppress=False)
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
rand_arr

# Exercise 9: Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)
arr
arr[:, [1,0,2]]

# Exercise 10: Swap rows 1 and 2 in the array arr:
arr = np.arange(9).reshape(3,3)
arr
arr[[1,0,2], :]