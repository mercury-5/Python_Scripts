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

