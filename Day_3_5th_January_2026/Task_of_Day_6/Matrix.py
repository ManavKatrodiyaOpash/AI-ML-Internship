import numpy as np

#Matrix Operations
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr2 = np.array([[1, 7, 3],
                 [8, 3, 6],
                 [9, 1, 3]])

print(arr1)
print(arr2)

# matrix numeric operation
arr_add = np.add(arr1, arr2)
print(arr_add)

arr_sub = np.subtract(arr1, arr2)
print(arr_sub)

arr_mul = np.multiply(arr1, arr2)
print(arr_mul)

print(np.dot(arr1, arr2))  #this is real multiplication of matrix the dot product

arr_div = np.divide(arr1, arr2)
print(arr_div)

print(np.identity(3))

# aggregation
print(np.sum(arr1))
print(np.mean(arr1, axis=0))