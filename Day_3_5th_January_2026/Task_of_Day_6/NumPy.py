import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(arr_2d)

# slicing
print(arr_2d[0:2][1:3])

# indexing
print(arr_2d[2])

# The Checkerboard: Create an 8X8 matrix and fill it with a checkerboard pattern of 0s and 1s (hint: use slicing with steps [::2]).

print("\n Task 1 :-\n \t The Checkerboard: Create an 8X8 matrix and fill it with a checkerboard pattern of 0s and 1s (hint: use slicing with steps [::2]).\n\n")

checker_board = np.zeros((8, 8))
checker_board[::2, ::2] = 1
checker_board[1::2, 1::2] = 1
print(checker_board)

# Broadcasting: Create a 5X5 matrix where each row has values ranging from 0 to 4. (Hint: Add a 1D array [0, 1, 2, 3, 4] to a 5X1 column of zeros).

print("\n Task 2 :- \n \t Broadcasting: Create a 5X5 matrix where each row has values ranging from 0 to 4. (Hint: Add a 1D array [0, 1, 2, 3, 4] to a 5X1 column of zeros).\n\n")

broadcast_arr = np.zeros((5, 5))
arr_add = np.array([0, 1, 2, 3, 4])
print(broadcast_arr)

result = broadcast_arr + arr_add
print(result)


# Normalization: Create a random 5X5 matrix and normalize it. Normalization means subtracting the mean and dividing by the standard deviation: Z = (x - mu)/sigma :- mu = means, sigma = standard deviation

print("\n Task 3 :- \n \t Normalization: Create a random 5X5 matrix and normalize it. Normalization means subtracting the mean and dividing by the standard deviation: Z = (x - mu)/sigma :- mu = means, sigma = standard deviation\n\n")

arr_norm = np.random.randint(1, 10, (5, 5))
print(arr_norm)

mu = arr_norm.mean()
sigma = arr_norm.std()

norm = (arr_norm - mu)/sigma
print(norm)

# The Border: Create a 5X5 matrix of ones and change the "padding" (the outermost rows and columns) to zeros without using a loop.

print("\n Task 4 :- \n \t The Border: Create a 5X5 matrix of ones and change the 'padding' (the outermost rows and columns) to zeros without using a loop.\n\n")

arr_bord = np.ones((5, 5))
print(arr_bord)

arr_bord[0,:] = 0
arr_bord[-1,:] = 0
arr_bord[:,0] = 0
arr_bord[:,-1] = 0

print(arr_bord)


# The Conditional Filter (Boolean Indexing)
# Task:
# Create a 10X10 matrix of random integers between 1 and 100.
# Find all values in the matrix that are greater than 50.
# Replace all those values with the number 999.Why? In data cleaning, we often need to replace "outliers" or invalid data points based on a condition.

print("\n Task 5 The Conditional Filter (Boolean Indexing):- \n \t Create a 10X10 matrix of random integers between 1 and 100. \n \t Find all values in the matrix that are greater than 50. \n \t Replace all those values with the number 999.Why? In data cleaning, we often need to replace 'outliers' or invalid data points based on a condition.\n\n")

arr = np.random.randint(1, 100, (10, 10))
print(arr)
for i in range(len(arr[0])):
    for j in range(len(arr)):
        if arr[i][j] > 50:
            print(f"The value greather than 50 found at position ({i},{j}) is {arr[i][j]}")
            arr[i][j] = 999
print(arr)

# Task 6: The Column-wise Summary (Axis Operations)
# Task:
# Create a 4X5 matrix.
# Calculate the sum of each column.
# Calculate the maximum value of each row.
# Why? In data analysis, we often need to summarize features (columns) or observations (rows) separately.

print("\n Task 6 The Column-wise Summary (Axis Operations):- \n \t Create a 4X5 matrix. \n \t Calculate the sum of each column. \n \t Calculate the maximum value of each row. \n \t Why? In data analysis, we often need to summarize features (columns) or observations (rows) separately.\n\n")

arr = np.random.randint(1, 100, (4, 5))
print(arr)

for i in range(len(arr[0])):
    print(f"Sum of elements of {i+1} column is {np.sum(arr[:,i])}")

# Task 7: The Fancy Diagonal
# Task:
# Create a 5X5 matrix of zeros.
# Change the main diagonal (top-left to bottom-right) to [1, 2, 3, 4, 5].
# Change the anti-diagonal (top-right to bottom-left) to [1, 1, 1, 1, 1].
# Why? Diagonal matrices are fundamental in linear algebra for scaling and transformations.

print("\n Task 7: The Fancy Diagonal:- \n \t Create a 5X5 matrix of zeros. \n \t Change the main diagonal (top-left to bottom-right) to [1, 2, 3, 4, 5]. \n \t Change the anti-diagonal (top-right to bottom-left) to [1, 1, 1, 1, 1]. \n \t Why? Diagonal matrices are fundamental in linear algebra for scaling and transformations.\n\n")

arr = np.zeros((5, 5))
np.fill_diagonal(arr, [1,2,3,4,5])
arr[:,::-1][np.diag_indices(5)] = 1
print(arr)


# Task 8: Vectorized Comparison
# Task:
# Create two random 1D arrays, A and B, both of size 10.
# Create a third array C that contains only the values that are the same in both A and B at the same position.
# Why? Identifying matching indices is key for comparing different model predictions or datasets.

print("\n Task 8: Vectorized Comparison:- \n \t Create two random 1D arrays, A and B, both of size 10. \n \t Create a third array C that contains only the values that are the same in both A and B at the same position. \n \t Why? Identifying matching indices is key for comparing different model predictions or datasets.\n\n")

arr1 = np.array([1,2,3,4,5,7,8,9,10])
arr2 = np.array([1,3,4,4,6,7,8,9,5])
print(arr1)
print(arr2)
mask = (arr1 == arr2) # Create a Boolean Mask where elements are equal at the same index
arr3 = arr1[mask] # Use the mask to get the values from either array
print(arr3)

# Task 9: Reshaping & Stacking
# Task:
# Create a 1D array of 20 elements (0 to 19).
# Reshape it into a 4X5 matrix.
# Split it into two 2X5 matrices.
# Stack them back horizontally to create a 2X10 matrix.
# Why? Data often arrives in the 'wrong' shape and needs restructuring before being fed into ML models.

print("\n Task 9: Reshaping & Stacking:- \n \t Create a 1D array of 20 elements (0 to 19). \n \t Reshape it into a 4X5 matrix. \n \t Split it into two 2X5 matrices. \n \t Stack them back horizontally to create a 2X10 matrix. \n \t Why? Data often arrives in the 'wrong' shape and needs restructuring before being fed into ML models.\n\n")

arr = np.array([c for c in range(20)]).reshape(4, 5)
print(arr)

small_arr1,small_arr2 = np.split(arr, [2])
print(small_arr1)
print(small_arr2)
modified_arr = np.hstack((small_arr1, small_arr2))
print(modified_arr)