import numpy as np

array = np.array([3, 6, 9, 12])
division = array/3
print(division)
print (type(division))

# 2D Array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

for x in arr:
    print(x)

i = 0
while i < len(arr):
    print(arr[i])
    i += 1