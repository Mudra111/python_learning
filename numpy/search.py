import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# Search for element equal to 5
x = np.where(arr == 5)
print(arr)
print(x)
print(x[0])
print(arr[x[0]])

# Search for elements greater than and equal to 6
y = np.where(arr >= 6)
print(y)
print(y[0])
print(arr[y[0]])

# Search for odd or even itens
odd = np.where(arr % 2 == 1)
print(odd)
print(odd[0])
print(arr[odd[0]])

even = np.where(arr % 2 == 0)
print(even)
print(even[0])
print(arr[even[0]])