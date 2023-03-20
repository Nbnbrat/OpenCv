import numpy as np

arr = np.array([(1,2,3,4),(14,5,6,8)])
print(arr[1,::])
arr1 = arr.reshape(1,8)
print(arr1)

arr2 = np.array([1,2,3,4,14,5,6,8])
print(arr2.reshape(4,2))
print(np.append(arr1,80))
print(np.delete(arr1,1))
print(arr1.ravel()) # flattenning the array into single vector
arr3 = np.array([1,2,3,4,14,5,6,8])
arr4 = np.array([1,6,3,4])
print(np.concatenate((arr2,arr3)))
arr5 = np.copy(arr1)
print(arr5)