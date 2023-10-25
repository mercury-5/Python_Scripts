#!/usr/bin/env python3

# Ask the user upto which to print Fibonacci series
limit = input("Enter a number upto which to print Fibonacci series: ")

# Warn the user upon invalid inpu
try:
    limit = int(limit) # Convert limit to integer
except ValueError:
    print("Invalid input! Please enter a valid integer only!")

# Empty list to store the series
fib_series = []

# Initialize the first members of the series
a = 0
b = 1

# Append the first values to the list
fib_series.extend([a, b])

# Generate the rest of numbers in the series
while b <= limit:
    c = a + b
    if c <= limit:
        fib_series.append(c)
    
    a, b = b, c

# Convert the list into string
fib_str = ' '.join(map(str, fib_series))

# Print the series
print(f"Fibonacci series upto {limit} is: {fib_str}")