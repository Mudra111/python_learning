import numpy as np

num = np.array([1,4,3,7,9,6,8,2,5,0])
alpha = np.array(["cat","ox","dog","yak","cow","got","snak"])
boolean = np.array([True, False, True, False])


print(np.sort(num))
print(np.sort(alpha))
print(np.sort(boolean))

arr = np.array([[2,7,4,9],[5,0,3,1]])
print(np.sort(arr))