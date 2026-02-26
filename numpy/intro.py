import numpy as np

# python lists
list1 = [1,2,3,4,5]
print(list1)

# python list can have elements of multiple data types
list2 = ['mudra', 1,2,3,0, True, False]
print(list2)

# access list element with index
print(list2[3])


# Numpy - Numeric Python
# ndarray - n-dimentional array
arr1 = np.array([1,2,3,4,5,6,7])
print(arr1)

# shape - same as length
print(arr1.shape)

# arange - create numpy array (same as range)
arr2 = np.arange(10)
print(arr2)

# arange - (start, stop(not included), step)
arr3 = np.arange(0,10,3)
print(arr3)

# Zeros - create an array of zeros
arr4 = np.zeros(10)
print(arr4)

# Multidimentional zeros (dimention, number of element in each dimention)
arr5 = np.zeros((3,10))
print(arr5)

# full - create a multi-dimentional array with given values - (shape, fill_value, dtype = None, order = 'C')
arr6 = np.full([5,10],20,dtype=int)
print(arr6)

# access element in numpy array
print(arr6[0][9])

# python list to numpy array
list3 = [1,2,3,4,5]
arr7 = np.array(list3)
print(arr7)