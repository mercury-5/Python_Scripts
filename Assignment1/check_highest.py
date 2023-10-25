#!/usr/bin/env python3

# Initialize an empty list to store user inputs
input_list = []

# Ask the user to give inputs
while True:
    in_val = input("Enter numbers to find highest betwen them ('q' to quit): ")

    if in_val.lower() == 'q':
        break

    # Warn the user for invalid inputs
    try:
        in_val = float(in_val) # Convert the input to float
    except ValueError:
        print("Invalid input! Please enter numbers only!")
        continue

    input_list.append(in_val)

# Check if the list is not empty
if input_list:
    highest_val = max(input_list)
    print(f"Highest of them all is: {highest_val}")
else:
    print("List is empty!")