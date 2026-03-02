import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# Using for loop
# 1D array iterate
for i in arr1:
    print(i)

# 2D array iterate
for i in arr2:
    for j in i:
        print(j)

# 3D array iterate
for i in arr3:
    for j in i:
        for k in j:
            print(k)


# Using np.nditer()
# 1D
for i in np.nditer(arr1):
    print(i)

# 2D
for i in np.nditer(arr2):
    print(i)

# 3D
for i in np.nditer(arr3):
    print(i)