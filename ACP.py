# 1. Working with an Array (List in Python)
my_array = [10, 20, 30, 40, 50]
print("Original Array:", my_array)

# Accessing elements by index (0-based)
print("First Element:", my_array[0])
print("Last Element:", my_array[-1])

# Adding and removing elements
my_array.append(60)
print("After append(60):", my_array)

my_array.pop()
print("After pop():", my_array)
reversed_slicing = my_array[::-1]
print("\nReversed (using slicing):", reversed_slicing)