# Example of bitwise AND (&)
# Performs a binary AND operation between two numbers.
# For example: 5 (0101 in binary) & 3 (0011 in binary) = 1 (0001 in binary).
a = 5
b = 3
result_and = a & b
print("Bitwise AND:", result_and)  # Output: 1

# Example of bitwise OR (|)
# Performs a binary OR operation between two numbers.
# For example: 5 (0101 in binary) | 3 (0011 in binary) = 7 (0111 in binary).
result_or = a | b
print("Bitwise OR:", result_or)  # Output: 7

# Example of bitwise XOR (^)
# Performs a binary XOR operation between two numbers (1 if bits differ, 0 if the same).
# For example: 5 (0101 in binary) ^ 3 (0011 in binary) = 6 (0110 in binary).
result_xor = a ^ b
print("Bitwise XOR:", result_xor)  # Output: 6

# Example of bitwise NOT (~)
# Flips all the bits of the number (1's complement). Note: In Python, it also changes the sign.
# For example: ~5 (0101 in binary) = -6 (all bits flipped and sign changed).
result_not = ~a
print("Bitwise NOT:", result_not)  # Output: -6

# Example of bitwise left shift (<<)
# Shifts the bits of the number to the left by the specified number of positions (multiplies by 2^positions).
# For example: 5 (0101 in binary) << 1 = 10 (1010 in binary).
result_left_shift = a << 1
print("Bitwise Left Shift:", result_left_shift)  # Output: 10

# Example of bitwise right shift (>>)
# Shifts the bits of the number to the right by the specified number of positions (divides by 2^positions).
# For example: 5 (0101 in binary) >> 1 = 2 (0010 in binary).
result_right_shift = a >> 1
print("Bitwise Right Shift:", result_right_shift)  # Output: 2