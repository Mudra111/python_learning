import numpy as np

arr = np.array([1,2,3,4,5])
copy = arr.copy()
view = arr.view()

# Change the array
arr[0] = 10
print('After changing array : ')
print(f'Array {arr}')
print(f'View {view}')
print(f'Copy {copy}')
print('-----------------')

# Change copy
copy[1] = 20
print('After changing copy : ')
print(f'Array {arr}')
print(f'View {view}')
print(f'Copy {copy}')
print('-----------------')

# Change view
view[2] = 30
print('After changing view : ')
print(f'Array {arr}')
print(f'View {view}')
print(f'Copy {copy}')
print('-----------------')