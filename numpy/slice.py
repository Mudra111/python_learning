import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# Slicing [start:end(not included):steps]
print(arr[0:5]) # Return 1,2,3,4,5

print(arr[0:5:2]) # Return 1,3,5

print(arr[::3]) # Return 1,4,7,10

# Not given end , it'll goes up until last element
print(arr[3:]) # Return 4,5,6,7,8,9,10

# give negative step it'll start from the end of the array
print(arr[::-1]) # Return reverse of the array 

# Negative index 
print(arr[-3:-1]) # Return 8,9

# Negative start,end,step
print(arr[-2:-7:-1]) # Return 9,8,7,6,5


# Slicing in 2-d array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# pull slice of only 1st element
print(arr2[0:1,1:4]) # Return 2,3,4

# pull slice of both element
print(arr2[0:,0:4]) # Return 1,2,3,4 6,7,8,9