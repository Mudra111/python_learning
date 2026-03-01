import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

reshaped_arr = np.reshape(arr, (2,4))
print(reshaped_arr)

reshaped_arr2 = np.reshape(arr, (2,2,2))
print(reshaped_arr2)

# -1 to auto calculate number of rows according to number of elements and given dimention
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped_arr3 = np.reshape(arr2, (3,-1,2))
print(reshaped_arr3)

reshaped_arr4 = np.reshape(arr2, (-1, 3))
print(reshaped_arr4)

# flatten to 1-D
reshape_1d = np.reshape(reshaped_arr3,(-1))
print(reshape_1d)

