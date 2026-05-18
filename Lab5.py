# Lab 5: WAP that creates a 3x3 NumPy array of random integers between 1 and 100.

import numpy as np

# Create a 3x3 NumPy array with random integers from 1 to 100
array = np.random.randint(1, 101, (3, 3))

# Display the array
print("3x3 Random Integer Array:")
print(array)