import numpy as np

# Setup: Import NumPy.
# Creation: Create a 5X5 matrix of random integers between 1 and 100.
# Indexing: Extract the "inner" 3X3 grid from that 5X5 matrix.
# Math: Create a 3X3 identity matrix and add it to your extracted grid.
# Statistics: Calculate the mean and standard deviation of the resulting matrix.

big_arr = np.random.randint(1, 101, size=(5, 5))

print(f"Original 5X5 Matrix :-\n{big_arr}")

small_arr = big_arr[1:4,1:4]
print(f"\nExtracted 3X3 Matrix :-\n{small_arr}")

id_arr = np.identity(3)

modified_arr = small_arr + id_arr
print(f"\nModified Matrix :-\n{modified_arr}")

print(f"Mean of this new modefied matrix is :- {np.mean(modified_arr)}")
print(f"Standard deviation of this new modefied matrix is :- {np.std(modified_arr)}")