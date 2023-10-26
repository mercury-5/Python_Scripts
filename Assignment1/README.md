# Script Documentation
## 1. Number addition script

`add_nums.py`: This simple Python script asks the user to input three numbers and calculates their sum. It performs input validation to ensure the user enters valid numbers. If the user provides invalid input, they will be prompted to re-enter the numbers.

## How to Use

1. Run the script.
2. Enter the first number when prompted.
3. Enter the second number when prompted.
4. Enter the third number when prompted.
5. The script will calculate and display the sum of the three numbers.
6. The script will continue to execute until you provide valid input.

## 2. Array2String and String2Array script

`array_to_string.py`: This Python script allows you to perform two operations: converting a user-provided string into an array and converting the array back into a string.

## How to Use

1. Run the script.
2. Enter any string when prompted.
3. The script will convert the input string into an array, separating words based on spaces.
4. It will display the resulting array.
5. The script will then convert the array back into a string, joining the elements with spaces.
6. It will display the reconstructed string.

## 3. Binary number conversion & operations

`bin_conv.py`: This Python script allows you to perform various operations on binary numbers, including converting them to decimal and octal, as well as finding the 1's and 2's complement.

## How to Use

1. Run the script.
2. Enter a valid binary number when prompted.
3. The script will perform the following operations:
   - Convert the binary input to decimal and display the result.
   - Convert the binary input to octal and display the result.
   - Find and display the 1's complement of the binary input.
   - Find and display the 2's complement of the binary input.
4. The script will continue to execute until a valid binary input is provided.

## Binary Input Validation

The script validates the input to ensure it is a valid binary number (comprised of 0s and 1s) and provides appropriate warnings for invalid inputs.

## 4. Checking for highest number

`check_highest.py`: This Python script allows you to perform various operations on binary numbers, including converting them to decimal and octal, as well as finding the 1's and 2's complement.

## How to Use

1. Run the script.
2. Enter a valid binary number when prompted.
3. The script will perform the following operations:
   - Convert the binary input to decimal and display the result.
   - Convert the binary input to octal and display the result.
   - Find and display the 1's complement of the binary input.
   - Find and display the 2's complement of the binary input.
4. The script will continue to execute until a valid binary input is provided.

## Binary Input Validation

The script validates the input to ensure it is a valid binary number (comprised of 0s and 1s) and provides appropriate warnings for invalid inputs.

## 5. Prime number checking

`check_prime.py`: This Python script allows you to check whether a given number is a prime number or not. It takes an integer as input and evaluates whether the input number is prime. It will then display the result.

## How to Use

1. Run the script.
2. Enter an integer to check if it is a prime number.
3. The script will validate the input, ensuring it is a valid integer. If an invalid input is provided, the script will display a warning.
4. If the input is less than or equal to 1, the script will confirm that it's not a prime number.
5. If the input is 2, it will confirm that it's a prime number.
6. For any other positive integer, the script will calculate whether it is prime or not and provide the result.
7. The script will display whether the entered number is prime or not.

## Input Validation

The script validates the input to ensure it is a valid integer, and it provides feedback for invalid inputs.

## 6. Fibonacci Series generation

`fibonacci_srs.py`: This Python script generates a Fibonacci series up to a specified limit. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

## How to Use

1. Run the script.
2. Enter a number to specify up to which point you want to print the Fibonacci series.
3. The script validates the input to ensure it is a valid integer. If you provide an invalid input, it will display a warning.
4. The script generates the Fibonacci series up to the specified limit.
5. The resulting Fibonacci series is presented as a space-separated string.

## Input Validation

The script validates the input to ensure it is a valid integer and provides feedback for invalid inputs.

## 7. IPv4 Address generation

`ip_gen.py`: This Python script generates IPv4 addresses within a specified range. IPv4 addresses consist of four octets, each ranging from 0 to 255. This script allows you to specify a lower and upper bound and generates all valid IPv4 addresses within that range.

## How to Use

1. Run the script.
2. The script will ask you to enter the lower and upper bounds of the IPv4 range. Enter these values when prompted.
3. The script validates your input to ensure they are valid IPv4 addresses.
4. If the input is valid, the script generates all IPv4 addresses within the specified range.
5. The resulting IPv4 addresses are displayed one per line.

## Input Validation

The script validates your input to ensure it is a valid IPv4 address. If you provide an invalid input, it will display a warning.

## 8. IPv4 Address validation

`ip_validation.py`: This Python script allows you to check whether an input string is a valid IPv4 address or not. It uses the `socket.inet_aton` function to verify if the entered string is a valid IP address.

## How to Use

1. Run the script.
2. The script will prompt you to enter an IP address or 'q' to quit.
3. Enter the IP address you want to validate.
4. The script will check if the input is a valid IPv4 address.
5. It will display a message indicating whether the input is a valid IP address or not.

## Input Validation

The script uses the `socket.inet_aton` function to validate the IP address format. If the input is a valid IPv4 address, it will confirm that. If the input is not a valid IP address, the script will notify you accordingly.

## 9. Prime numbers in a particular range

`prime_in_range.py`: This Python script allows you to find prime numbers within a specified range. It prompts you to enter the lower and upper bounds of the range and then calculates and displays the prime numbers within that range.

## How to Use

1. Run the script.
2. The script will ask you to enter the lower bound of the range.
3. Enter the lower bound (an integer).
4. Next, you'll be prompted to enter the upper bound of the range.
5. Enter the upper bound (an integer).
6. The script will then calculate and display the prime numbers between the specified range.
7. It will also provide the count of prime numbers found within the range.

## Prime Number Calculation

The script uses a basic algorithm to identify prime numbers within the given range. It checks each number in the range and determines if it's a prime by testing for divisibility by numbers between 2 and the square root of the number. If a number is not divisible by any other number in that range, it's considered prime.

## 10. String sorting

`sort_string.py`: This Python script allows you to enter a string, and it will sort and display the characters in both ascending and descending orders.

## How to Use

1. Run the script.
2. The script will prompt you to enter a string.
3. Enter the string you want to sort.

The script will then sort the characters in the entered string in two ways and display the results:

- Ascending Order: The characters sorted in ascending alphabetical order.
- Descending Order: The characters sorted in descending alphabetical order.

## Sorting Mechanism

The script sorts the characters in the string using Python's built-in `sorted` function. It converts the sorted lists back to strings for display.