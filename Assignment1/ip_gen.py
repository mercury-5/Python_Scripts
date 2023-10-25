#!/usr/bin/env python3

import socket

# Function to generate IPv4 addresses within a range
def gen_ip(start_ip, end_ip):
    # Empty list to store the generated IPv4 addresses
    ip_address = []

    # Split the octets and store them as integers
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))

    while start <= end:
        ip_address.append('.'.join(map(str, start)))

        # Increase the last octet
        start[3] += 1

        # Check for carryover in each octet
        for i in range(3, 0, -1):
            if start[i] == 256:
                start[i] = 0
                start[i - 1] += 1

    return ip_address

# Function to validate user-entered range
def ip_validation(input_ip):
    try:
        socket.inet_aton(input_ip)
        return True
    except socket.error:
        return False
    
while True:
    # Ask the user to enter the lower bound of IPv4
    lower_ip = input("Enter the lower bound of IPv4 ('q' to quit): ")

    # Quit the script if the user presses 'q'
    if lower_ip.lower() == 'q':
        break

    # Warn the user for an invalid IPv4
    if not ip_validation(lower_ip):
        print("Invalid IPv4 address! Please enter a correct one or 'q' to quit!")
        continue

    # Ask the user to enter the upper bound of IPv4
    upper_ip = input("Enter the upper bound of IPv4 ('q' to quit): ")

    # Quit the script if the user presses 'q'
    if upper_ip.lower() == 'q':
        break

    # Warn the user for an invalid IPv4
    if not ip_validation(upper_ip):
        print("Invalid IPv4 address! Please enter a correct one or 'q' to quit!")
        continue

    generated_addresses = gen_ip(lower_ip, upper_ip)
    print(f"Generated IPv4 addresses between {lower_ip} & {upper_ip} are:")
    print("\n".join(generated_addresses))
    break