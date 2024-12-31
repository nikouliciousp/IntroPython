import numpy as np

# Example 1: Creating a 1D NumPy array
array = np.array([1, 2, 3, 4, 5])
print("Created 1D NumPy array:", array)  # Printing the created array

# Example 2: Performing basic operations
array_addition = array + 10  # Adding 10 to each element
print("Array after addition:", array_addition)

array_multiplication = array * 2  # Multiplying each element by 2
print("Array after multiplication:", array_multiplication)

# Example 3: Using NumPy functions
mean_value = np.mean(array)  # Calculating the mean
print("Mean of the array:", mean_value)

reshaped_array = array.reshape(1, 5)  # Reshaping the array to 1 row and 5 columns
print("Reshaped array (1x5):", reshaped_array)

# Example 4: Creating a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Created 2D NumPy array:\n", array_2d)  # Printing the 2D array

# Example 5: Slicing a NumPy array
sliced_array = array_2d[:, 1]  # Slicing to get the second column
print("Sliced array (second column):", sliced_array)

# Example 6: Dot product of two arrays
array1 = np.array([1, 2])
array2 = np.array([3, 4])
dot_product = np.dot(array1, array2)  # Calculating dot product
print("Dot product of array1 and array2:", dot_product)

# Example 7: Calculating standard deviation
std_deviation = np.std(array_2d)  # Calculating the standard deviation
print("Standard deviation of the 2D array:", std_deviation)