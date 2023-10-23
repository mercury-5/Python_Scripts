#!/usr/bin/env python3

import csv

# Function to read the CSV file & convert it into hash
def hash_reader(database_file):
    top_hash = {}

    with open(database_file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            serial = int(row['Serial'])
            item = row['Item']
            price = int(row['Price'])

            if serial not in top_hash:
                top_hash[serial] = {}
            
            top_hash[serial][item] = price

    return top_hash

# Function to print the restaurant menu
def restaurant_menu(menu_hash):
    print ("╔═════════╦═══════════════════════════════════════════╦═════════╗")
    print ("║ Sl. No. ║                   Items                   ║  Price  ║")
    print ("╠═════════╬═══════════════════════════════════════════╬═════════╣")

    for serial in sorted(menu_hash.keys()):
        serial_dict = menu_hash[serial]
        for item, price in serial_dict.items():
            # Center-align text within each cell
            serial_str = str(serial).center(9)
            item_str = item.center(43)
            price_str = str(price).center(9)
            print(f"║{serial_str}║{item_str}║{price_str}║")
    print("╚═════════╩═══════════════════════════════════════════╩═════════╝")

# Function to take order from customer
def take_order(menu_hash):
    # Empty hash to store the order
    order_hash = {}

    while True:
        # Display the menu by calling the function
        restaurant_menu(menu_hash)
        choice = input("Enter your choice (q to quit):").lower()
        
        # Check for the entered input if it is 'q' then stop the script
        if choice == "q":
            break

        try:
            choice = int(choice)  # Convert choice to an integer
        except ValueError:
            print("Invalid item! Please select a valid item!")
            continue

        # Warn the user if the serial number is not in the menu
        if choice not in menu_hash.keys():
            print("Invalid item! Please select a valid item!")
            continue

        item_info = menu_hash[choice]
        item_name = list(item_info.keys())[0]
        item_price = item_info[item_name]

        quantity = input(f"Enter the quantity of {item_name}:")

        # Warn the user if the quantity is not an integer or if the quantity is negative
        if not quantity.isdigit() or int(quantity) < 1:
            print("Invalid quantity! Please enter a valid quantity!")
            continue

        # Store the order in the hash
        order_hash[item_name] = {"quantity": int(quantity), "price": item_price}
    
    return order_hash

# Function to calculate the bill with 18% GST
def calculate_bill(order_hash):
    sub_total = 0
    GST = 0.18

    for item, item_info in order_hash.items():
        item_price = item_info["price"]
        item_qunatity = item_info["quantity"]

        item_total = item_qunatity * item_price
        sub_total += item_total
    
    # Calculate GST
    tax = sub_total * GST
    grand_total = sub_total + tax

    return {
        "sub_total": sub_total,
        "tax": tax,
        "total": grand_total,
    }

# Function to print the bill beautifully with order summary
def print_bill(order_hash, bill_info):
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                       Restaurant Bill                         ║")
    print("╟───────────────────────────────────────────────────────────────╢")
    print("║ {:<30} {:<10} {:<10} {:<8} ║".format("Item", "Quantity", "Price", "Total"))
    print("╟───────────────────────────────────────────────────────────────╢")

    sub_total = 0

    for item, item_data in order_hash.items():
        quantity = item_data["quantity"]
        price = item_data["price"]
        total = quantity * price
        sub_total += total
        print("║ {:<30} {:<10} {:<10} {:<8} ║".format(item, quantity, price, total))

    print("╟───────────────────────────────────────────────────────────────╢")
    print("║ {:<30} {:<10} {:<10} {:<8} ║".format("Sub Total:", "", "", sub_total))
    print("║ {:<30} {:<10} {:<10} {:<8.2f} ║".format("Tax (18%):", "", "", bill_info["tax"]))
    print("║ {:<30} {:<10} {:<10} {:<8.2f} ║".format("Total:", "", "", bill_info["total"]))
    print("╚═══════════════════════════════════════════════════════════════╝")

# Call the function to read the csv file
menu_file = "restaurant_menu.csv"
menu_hash = hash_reader(menu_file)

# Take the order from the user
print("***************[Welcome to XYZ Family Restaurant]***************")
order_hash = take_order(menu_hash)

# Calculate the bill
bill_info = calculate_bill(order_hash)

# Check if the user ordered anything
if order_hash:
    # User ordered something, so print the bill
    print_bill(order_hash, bill_info)
    message = "Thank you! Visit again ^_^"
    centered_message = f"{message:^65}"
    print(centered_message)
else:
    # User didn't order anything, so prompt "Goodbye"
    print("\nGoodbye! Thank you for visiting XYZ Family Restaurant\n")