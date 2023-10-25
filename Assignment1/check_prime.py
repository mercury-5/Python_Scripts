#!/usr/bin/env python3

import math

# Ask the user to enter in_valber to check prime
in_val = input("Enter number to check prime or not: ")

# Warn the user upon invalid input
try:
    in_val = int(in_val)  # Convert in_val to an integer
except ValueError:
    print("Invalid input! Please enter a valid integer only!")

if in_val <= 1:
    print(f"{in_val} is not prime")
elif in_val == 2:
    print(f"{in_val} is prime number")
else:
    flag = True
    for i in range (2, int(math.sqrt(in_val)) + 1):
        if in_val % i == 0:
            flag = False
    if flag:
        print(f"{in_val} is prime")
    else:
        print(f"{in_val} is not prime")