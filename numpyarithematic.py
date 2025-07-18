import numpy as np

arr1 = np.array([[1,2],
                 [5,6]])
arr2 = np.array([[9,10],
                  [13,14]])
print(np.add(arr1,arr2))
print()
print(np.subtract(arr1,arr2))
print()
print(np.multiply(arr1,arr2))
print()
print(np.divide(arr1,arr2))
print()
print(np.dot(arr1,arr2))
print()
print(arr1.transpose())
print()
print(arr1.trace())