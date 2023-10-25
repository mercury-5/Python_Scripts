#!/usr/bin/env python3

import socket

# Function to validate the IP address entered by user
def ip_validation(input_ip):
    try:
        socket.inet_aton(input_ip)
        return True
    except socket.error:
        return False

while True:
    # Ask the user to enter an IP address
    ip_v4 = input("Enter an IP address ('q' to quit): ")

    if ip_v4.lower() == 'q':
        break

    # Call the function to verify
    if ip_validation(ip_v4):
        print(f"{ip_v4} is a valid IP address")
    else:
        print(f"{ip_v4} is not a valid IP address")