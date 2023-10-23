# Python Script Documentation

This is a Python script that performs various operations on a student database in CSV format. The script includes functions for reading the CSV file, calculating total marks for each student, printing students in ranking order, finding top students in each subject, calculating average marks in each subject, and more.

## Code Structure

- The code consists of several functions that serve different purposes.
- The main functions include:
  - `hash_reader(database_file)`: Reads the CSV file and converts it into a hash.
  - `calculate_mark(data_hash)`: Calculates total marks for each student.
  - `print_in_ranking_order(mark_hash)`: Prints students in ranking order.
  - `get_subject(data_hash)`: Extracts unique subject names from the database.
  - `print_top_student(data_hash)`: Finds and prints top students in each subject.
  - `calculate_avg_mark(subject, data)`: Calculates and prints average marks in each subject.
  - `print_total_mark(mark_hash)`: Prints total marks for each student.
  - `update_or_append(file_name, new_name, new_subject, new_mark)`: Updates or appends data in the database.
  - `remove_data(file_name, student_name)`: Removes an existing student from the database.
  - `print_prog_card(student, data)`: Prints a progress card for a student.

## Usage

You can use this script to perform various tasks related to a student database. To run the script, execute the main code at the bottom of the script file.

## Example Usage

```python
# Call the function to read the csv file
database_file = "database.csv"
data_hash = hash_reader(database_file)

# Calculate total marks
total_mark_hash = calculate_mark(data_hash)

# No.1: Total number of students
num_of_students = len(data_hash)
print(f"Total number of students: {num_of_students}")

# No.2: Students in ranking order
print_in_ranking_order(total_mark_hash)

# ... (and so on, you can uncomment and execute other parts of the code)
