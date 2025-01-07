import copy

original_list = [1, [1, 2, 3], 3]

shallow_copy = original_list[:]

deep_copy = copy.deepcopy(original_list)

original_list[0] = 4
shallow_copy[1][1] = 5
deep_copy[1][1] = 6

print(f"original list id: {id(original_list)}: {original_list}")
print(f"shallow copy id: {id(shallow_copy)}: {shallow_copy}")
print(f"deep copy id: {id(deep_copy)}: {deep_copy}")