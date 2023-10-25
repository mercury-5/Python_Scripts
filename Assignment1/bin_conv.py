#!/usr/bin/env python3

# Function to convert binary input to decimal
def bin2dec(bin_in):
    dec_val = 0
    power = len(bin_in) - 1

    for bit in bin_in:
        if bit == '1':
            dec_val += 2**power
        power -= 1
    return dec_val

# Function to convert binary input to decimal
def bin2oct(bin_in):
    dec_val = bin2dec(bin_in)
    oct_val = oct(dec_val).replace('0o', '')
    return oct_val

# Function to find 1's compliment
def comp_1s(bin_in):
    comp1s = bin_in.replace('0', 'x').replace('1', '0').replace('x', '1')
    return comp1s

# Function to find 2's compliment
def comp_2s(bin_in):
    comp1s = comp_1s(bin_in)
    dec_val = bin2dec(comp1s)
    comp2s = bin(dec_val + 1)[2:]
    comp2s = comp2s.zfill(len(bin_in))
    return comp2s

while True:
    # Ask the user to give binary input
    binary_in = input("Enter a binary number:")

    # Warn the user if not binary bits
    is_bin = all(bit in '01' for bit in binary_in)

    if is_bin:
        # Binary to decimal conversion
        dec_out = bin2dec(binary_in)

        # Binary to octal conversion
        oct_out = bin2oct(binary_in)

        # 1's compliment
        comp1s = comp_1s(binary_in)

        # 2's compliment
        comp2s = comp_2s(binary_in)

        print(f"Decimal value of {binary_in}: {dec_out}")
        print(f"Octal value of {binary_in}: {oct_out}")
        print(f"1's compliment of {binary_in}: {comp1s}")
        print(f"2's compliment of {binary_in}: {comp2s}")
        break
    else:
        print("Not a valid binary input! Please enter a valid binary input!")
        continue
