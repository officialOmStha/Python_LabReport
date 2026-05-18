'''Lab 9: WAP that converts the NumPy array to a Python list and sorts it using a lambda
function.'''

import numpy as np

# Create a 3x3 NumPy array with random integers from 1 to 100
array = np.random.randint(1, 101, (3, 3))

# Display original array
print("Original NumPy Array:")
print(array)

# Convert NumPy array to Python list
python_list = array.tolist()

# Flatten the nested list into a single list
flat_list = [item for row in python_list for item in row]

# Sort the list using lambda function
sorted_list = sorted(flat_list, key=lambda x: x)

# Display results
print("\nPython List:")
print(flat_list)

print("\nSorted List:")
print(sorted_list)