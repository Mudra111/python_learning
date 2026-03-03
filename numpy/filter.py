import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# Using boolean list
x = [True, False, False, True, True, False,True,True,False,True]
print(arr)
print(arr[x])

# Using for loop and boolean array
y = []
for i in arr:
    if i <= 5:
        y.append(True)
    else:
        y.append(False)

print(arr)
print(y)
print(arr[y])

# Using numpy shortcut
filter1 = (arr > 6) & (arr < 10)
print(arr)
print(filter1)
print(arr[filter1])

filter2 = arr > 6
print(arr)
print(filter2)
print(arr[filter2])