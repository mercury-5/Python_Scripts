#!/usr/bin/env python3

import re

# Function to check whether the entered password meets the criteria or not
def check_password(password, first_name, last_name, email_id, company_name):
    missing_conditions = []

    # Check if the password contains name or last name
    if re.search(re.escape(first_name), password, re.IGNORECASE) or re.search(re.escape(last_name), password, re.IGNORECASE):
        missing_conditions.append("Password must not contain your first name or last name")

    # Check if the password contains company name
    if re.search(re.escape(company_name), password, re.IGNORECASE):
        missing_conditions.append("Password must not contain your company name")       

    # Check if the password contains 8 characters or not
    if len(password) < 8:
        missing_conditions.append("Password must contain eight characters")

    # Check for at least one capital letter
    if not any(c.isupper() for c in password):
        missing_conditions.append("Password must contain one capital letter")

    # Check for at least one small letter
    if not any(c.islower() for c in password):
        missing_conditions.append("Password must contain one small letter")

    # Check for at least one number
    if not any(c.isdigit() for c in password):
        missing_conditions.append("Password must contain one number")

    # Check for at least one special character
    if not re.search(r'[#\$%&\'()*+,-/;;<=>?@^_^{}~]', password):
        missing_conditions.append("Password must contain one special character")

    # Check for more than two identical characters in a row
    if re.search(r'(.)\1{2}', password):
        missing_conditions.append("Password must not contain more than two identical characters in a row")

    # Check if the password contains the email domain and company name
    if re.search(r'@domain\.com', password, re.IGNORECASE):
        missing_conditions.append("Password must not contain the email domain")

    return missing_conditions

# Ask the user to enter his first name and last name to verify the password doesn't contain his name or last name
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

# Ask the user to enter his company name and email id to verify the password doesn't contain his company name or email id
company_name = input("Enter your company name:")
email_id = input("Enter your email id:")

# Extract the email domain from the email id
email_domain = email_id.split('@')[-1]

# Ask user to enter password
password = input("Enter your password:")
missing_condition = check_password(password, first_name, last_name, email_id, company_name)

if missing_condition:
    for condition in missing_condition:
        print(condition)
else:
    print("Password meets all criteria")