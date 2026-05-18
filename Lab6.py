''' Lab 6: WAP to compute row-wise sum, column-wise mean, and total standard deviation from
array of Lab 5. '''

import numpy as np

# Create a 3x3 NumPy array with random integers from 1 to 100
array = np.random.randint(1, 101, (3, 3))

# Display the array
print("Array:")
print(array)

# Row-wise sum
row_sum = np.sum(array, axis=1)

# Column-wise mean
column_mean = np.mean(array, axis=0)

# Total standard deviation
std_deviation = np.std(array)

# Display results
print("\nRow-wise Sum:")
print(row_sum)

print("\nColumn-wise Mean:")
print(column_mean)

print("\nTotal Standard Deviation:")
print(std_deviation)