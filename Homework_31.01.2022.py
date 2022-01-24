# Task 1 - list declaration

list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list)

# Task 2 - ascendant list

ascendant_list = sorted(list)
print(ascendant_list)

# Task 3 - descendant list

descendant_list = sorted(list, reverse=True)
print(descendant_list)

# Task 4 - a list of even numbers from the sorted list (using slice)

print(ascendant_list[1:11:2])

# Task 5 - a list of odd numbers from the sorted list (using slices)

print(ascendant_list[0:11:2])

# Task 6 - a list of numbers that are multiples of the number 3 (using slices)

print(ascendant_list[2:12:3])
