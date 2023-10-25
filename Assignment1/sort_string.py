#!/usr/bin/env python3

# Ask the user to enter a string
str_in = input("Enter a string: ")

# Sort the string in ascending order
sorted_asc = sorted(str_in)

# Sort the string in descending order
sorted_des = sorted(str_in, reverse=True)

# Convert the sorted list to string
sorted_asc_str = ' '.join(map(str, sorted_asc))
sorted_des_str = ' '.join(map(str, sorted_des))

# Print the sorted strings
print(f"Ascending order: {sorted_asc_str}")
print(f"Descending order: {sorted_des_str}")