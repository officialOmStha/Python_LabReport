# lab 1:

# Function to calculate sum, average, max, and min
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


# Taking input from the user
user_input = input("Enter integers separated by spaces: ")

# Convert input into a list of integers
original_list = list(map(int, user_input.split()))

# Ternary operator to check if the list is empty
print("The original list is empty."
      if len(original_list) == 0
      else "The original list is not empty.")

# Remove duplicates using set
unique_list = list(set(original_list))

# Sort the list in ascending order
unique_list.sort()

print("Sorted list without duplicates:", unique_list)

# Proceed only if the list is not empty
if len(unique_list) > 0:

    # Function call
    total, average, maximum, minimum = calculate_stats(unique_list)

    # Display results
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

    # Filter numbers greater than average
    greater_than_avg = []

    for num in unique_list:
        if num > average:
            greater_than_avg.append(num)

    print("Numbers greater than average:", greater_than_avg)