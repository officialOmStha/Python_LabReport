'''Lab 8: WAP that performs broadcasting: adds 10 to every element of the array.'''

import numpy as np

# Create a 3x3 NumPy array with random integers from 1 to 100
array = np.random.randint(1, 101, (3, 3))

# Display original array
print("Original Array:")
print(array)

# Broadcasting: Add 10 to every element
new_array = array + 10

# Display updated array
print("\nArray After Adding 10:")
print(new_array)