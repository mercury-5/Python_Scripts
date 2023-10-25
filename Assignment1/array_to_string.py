#!/usr/bin/env python3

# Ask the user to enter a string
user_input = input("Enter anything you want: ")

# Convert the user input string to array
str2array = user_input.split(' ')
print(f"String to array conversion: {str2array}")

# Convert the array back to string
array2str = ' '.join(str2array)
print(f"Array to string: {array2str}")