#!/usr/bin/env python3

import random

# Function to generate random password
def gen_pass():
    # Character sets for each required condition
    up_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_chars = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "#\$%&'()*+,-/;;<=>?@^_{}~"

    # Set password
    password = ""

    # Initialize the password with one character from each condition
    password = random.choice(up_chars) + random.choice(low_chars) + random.choice(digits) + random.choice(special_chars)

    # Remaining characters
    while len(password) < 8:
        char = random.choice(up_chars + low_chars + digits + special_chars)

        # Avoid two or more identical characters in a row
        if len(password) >= 2 and password[-1] == char and password[-2] == char:
            continue
        password += char
    
    return password

rand_pass = gen_pass()
print(f"Random password: {rand_pass}")