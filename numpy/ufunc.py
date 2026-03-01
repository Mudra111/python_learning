import numpy as np

arr = np.array([0,1,4,9,16,25,36,49,64,81,100])
arr2 = np.array([-3,-2,-1,0,1,2,3])
arr3 = np.array([10,20,30,40,50])
arr4 = np.array([1,2,3,4,5])

# Square root
print(np.sqrt(arr))

# Absolute
print(np.absolute(arr2))

# Exponent
print(np.exp(arr2))

# Min and Max
print(np.min(arr))
print(np.max(arr))

# Sign
print(np.sign(arr2))

# sin, cos, tan
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

# negative and positive
print(np.negative(arr2)) # will apply negative sign to every element
print(np.positive(arr2)) # will apply positive sign to every element

# add, subtract, multiply, divide, power, mod
print(np.add(arr3,arr4))
print(np.subtract(arr3,arr4))
print(np.multiply(arr3,arr4))
print(np.divide(arr3,arr4))
print(np.mod(arr3,arr4))