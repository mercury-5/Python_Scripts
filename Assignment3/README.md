# Script Documentation
## Restaurant Order Processing Script

`restaurant_biiling_script.py`: This Python script is designed to assist a restaurant in processing customer orders and generating bills. The script reads a menu from a CSV file, allows customers to select items, and calculates the bill with 18% GST. The final bill is beautifully formatted and displayed to the customer.

## Key Functions:

### 1. `hash_reader(database_file)`

- Reads a CSV file containing the restaurant's menu and converts it into a hash for easy access.

### 2. `restaurant_menu(menu_hash)`

- Prints the restaurant menu in a structured and easy-to-read format, including item names and prices.

### 3. `take_order(menu_hash)`

- Allows customers to place their orders by selecting items from the menu and specifying quantities.

### 4. `calculate_bill(order_hash)`

- Calculates the bill based on the items ordered, their quantities, and adds 18% GST.

### 5. `print_bill(order_hash, bill_info)`

- Prints the final bill with a detailed summary, including sub-total, tax (GST), and the grand total.

## How to Use:

1. Execute the script, and it will display the restaurant's menu.
2. Enter the item's serial number and quantity to add it to your order.
3. To finish your order, enter 'q'.
4. The script will calculate and display your bill with a breakdown of costs.

## Password Criteria Verification Script

`password_checker.py`: This Python script checks whether an entered password meets specific criteria to ensure security. It verifies that the password doesn't contain certain elements, follows length and character requirements, and adheres to security best practices.

## Key Functions:

### 1. `check_password(password, first_name, last_name, email_id, company_name)`

- Verifies that the password doesn't contain the user's first name, last name, company name, or email domain.
- Ensures that the password contains at least 8 characters, including a combination of capital and small letters, numbers, and special characters.
- Checks for the presence of more than two identical characters in a row.

### 2. User Input

- Asks the user to enter their first name, last name, company name, and email id.
- Extracts the email domain from the email id.

### 3. Password Validation

- Prompts the user to enter a password.
- Calls the `check_password` function to validate the password against the criteria.
- If the password doesn't meet the criteria, it lists the specific conditions that are not met.

## How to Use:

1. Execute the script.
2. Enter your first name, last name, company name, and email id as prompted.
3. Enter the password you want to validate.
4. The script will inform you if the password meets all the criteria or specify the conditions that are not met.

This script serves as a helpful tool for ensuring strong and secure passwords.

## Random Password Generator

`random_password.py`: This Python script generates a secure random password by combining characters from various character sets. It ensures that the password meets specific criteria, including a mix of uppercase letters, lowercase letters, digits, and special characters.

## Key Functions:

### 1. `gen_pass()`

- Generates a random password that meets the following criteria:
  - Contains at least one uppercase letter (A-Z).
  - Contains at least one lowercase letter (a-z).
  - Contains at least one digit (0-9).
  - Contains at least one special character from `#\$%&'()*+,-/;;<=>?@^_{}~`.
  - Avoids two or more identical characters in a row.

### 2. Password Generation

- Calls the `gen_pass` function to generate a random secure password.
- Prints the generated password.

## How to Use:

1. Execute the script.
2. The script will generate a random password that meets the specified criteria.
3. The generated password will be displayed in the output.

This script provides a quick and easy way to generate strong and secure passwords.

## Text Transformation Script

`sentence_transform.py`: This Python script provides text transformation functions to modify text in various ways. It can convert text to all capital letters, all small letters, capitalize the first letter of each word, make alternate letters of a word capital (with the word's first letter always capitalized), and make alternate letters capital.

## Key Functions:

### 1. `all_caps(text)`

- Converts the input text to all CAPITAL letters.

### 2. `all_small(text)`

- Converts the input text to all small letters.

### 3. `first_letter_caps(text)`

- Capitalizes the first letter of each word in the input text.

### 4. `alternate_word_caps(text)`

- Makes alternate letters of each word CAPITAL, with the word's first letter always CAPITAL.

### 5. `alternate_caps(text)`

- Makes alternate letters CAPITAL.

### 6. User Input and Output

- Prompts the user to enter text.
- Applies each transformation function to the input text.
- Prints the results for each transformation.

## How to Use:

1. Execute the script.
2. Enter the text you want to transform when prompted.
3. The script will apply each transformation function to the input text and display the results.

This script allows you to easily modify text according to different capitalization and formatting requirements.
