#!/usr/bin/env python3

import math

while True:
    # Ask the user to enter the lower and upper bound
    lower = input("Enter the lower bound of the range: ")

    # Warn the user for invalid inputs
    try:
        lower = int(lower) # Convert lower to int
    except ValueError:
        print("Invalid input! Please enter integer only!")
        continue

    upper = input("Enter the upper bound of the range: ")

    # Warn the user for invalid inputs
    try:
        upper = int(upper) # Convert upper to int
    except ValueError:
        print("Invalid input! Please enter integer only!")
        continue

    prime_count = 0 # Variable to keep track of number of prime numbers\
    prime = [] # Empty list to store prime numbers

    for i in range(lower, upper + 1):
        if i < 2:
            continue
        is_prime = True

        for j in range(2, int(math.sqrt(i) + 1)):
            if j % 2 == 0:
                is_prime = False
                break
        
        if is_prime:
            prime.append(i)
            prime_count += 1
    
    prime_str = ' '.join(map(str, prime))

    # Print the prime numbers and number count
    print(f"Prime numbers between {lower} & {upper} is: {prime_str}")
    print(f"Prime number count is: {prime_count}")
    break