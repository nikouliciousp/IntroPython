def bitwise_examples():
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary

    # Bitwise AND
    and_result = a & b  # 0000 -> 0

    # Bitwise OR
    or_result = a | b  # 1110 -> 14

    # Bitwise XOR
    xor_result = a ^ b  # 1110 -> 14

    # Bitwise NOT
    not_a = ~a  # Inverts all bits of a

    # Left Shift
    left_shift = a << 1  # Shifts bits of a left by 1 position -> 10100 (20)

    # Right Shift
    right_shift = a >> 1  # Shifts bits of a right by 1 position -> 0101 (5)

    print("Bitwise AND:", and_result)
    print("Bitwise OR:", or_result)
    print("Bitwise XOR:", xor_result)
    print("Bitwise NOT:", not_a)
    print("Left Shift:", left_shift)
    print("Right Shift:", right_shift)
