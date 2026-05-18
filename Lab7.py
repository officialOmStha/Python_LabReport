'''Lab 7: WAP which uses slicing to extract the second column and the last two rows from array
of Lab 5.'''

import numpy as np

# Create a 3x3 NumPy array with random integers from 1 to 100
array = np.random.randint(1, 101, (3, 3))

# Display the array
print("Original Array:")
print(array)

# Extract the second column
second_column = array[:, 1]

# Extract the last two rows
last_two_rows = array[-2:, :]

# Display results
print("\nSecond Column:")
print(second_column)

print("\nLast Two Rows:")
print(last_two_rows)