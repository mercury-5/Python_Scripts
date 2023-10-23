#!/usr/bin/env python3

import os
import csv

# Function to read the CSV file & convert it into hash
def hash_reader(database_file):
    top_hash = {}

    with open(database_file, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            name = row['Name']
            subject = row['Subject']
            marks = float(row['Marks'])

            if name not in top_hash:
                top_hash[name] = {}
            
            top_hash[name][subject] = marks

    return top_hash

# Function to calculate total marks for each student
def calculate_mark(data_hash):
    total_marks = {}

    for student, subjects in data_hash.items():
        total = 0
        for subject, marks in subjects.items():
            total += marks

        total_marks[student] = total

    return total_marks

# Function to print students in ranking order
def print_in_ranking_order(mark_hash):
    print("\n***********[Students in ranking order]************")

    # Sort the students by total marks in descending order
    sorted_student = sorted(mark_hash.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted students
    for name, marks in sorted_student:
        print(f"{name}: {marks}")

# Function to extract unique subject names from database
def get_subject(data_hash):
    unique_subjects = set(subject for subjects in data_hash.values() for subject in subjects)
    return list(unique_subjects)

# Function to find and print top students in each subject
def print_top_student(data_hash):
    print("\n**********[Top students in each subject]**********")

    # Get unique subject names   
    unique_subjects = get_subject(data_hash)

    for subject in unique_subjects:
        top_student = ""
        max_mark = 0

        for student, subjects in data_hash.items():
            marks = subjects.get(subject, 0) # Default to 0 if subject not found
            if marks > max_mark:
                max_mark = marks
                top_student = student
            elif marks == max_mark:
                top_student += f", {student}"
        print(f"Top student in {subject}: {top_student} (Marks: {max_mark})")

# Function to calculate and print average marks in each subject
def calculate_avg_mark(subject, data):
    print("\n**********[Average mark in each subject]**********")

    for sub in subject:
        total_mark = 0
        num_of_student = 0
        for student, subs in data.items():
            marks = subs.get(sub, 0) # Default to 0 if subject not found
            total_mark += marks
            num_of_student += 1
        if num_of_student > 0:
            avg_mark = total_mark / num_of_student
            print(f"Average marks in {sub}: {avg_mark:.2f}")
        else:
            print(f"No students found for {sub}")

# Function to print total marks for each student
def print_total_mark(mark_hash):
    print("\n**********[Total marks for each student]**********")
    for student, marks in total_mark_hash.items():
        print(f"Total marks for {student} is: {marks}")

# Function to update or append data in the database
def update_or_append(file_name, new_name, new_subject, new_mark):
    # Open the file in read mode to read existing data
    with open(file_name, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)

    found = False

    # Iterate through the lines and update or append data
    for i, line in enumerate(lines):
        name, sub, mark = line

        if name == new_name and sub == new_subject:
            # Update marks for existing entry
            found = True
            lines[i] = [new_name, new_subject, new_mark]

    # If not found, append a new entry
    if not found:
        lines.append([new_name, new_subject, new_mark])

    # Open the file in write mode to write data
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(lines)

# Function to remove an existing student from database
def remove_data(file_name, student_name):
    # Temporary file to store data
    temp_file = "temp.csv"

    # Open the original database file for reading data
    with open(file_name, 'r', newline='') as input_file:
        # Open the temporary file for writing
        with open(temp_file, 'w', newline='') as output_file:
            for line in input_file:
                name, _ = line.strip().split(',', 1)  # Extract the name from the line

                # Check if the student's name is not in the list of students to remove
                if name not in student_name:
                    output_file.write(line)

    # Replace the original file with the temporary file
    os.replace(temp_file, file_name)

# Function to print progress card for a student
def print_prog_card(student, data):
    print(f"Progress card for {student}:")
    print("╔════════════╦════════╗")
    print("║  Subject   ║  Marks ║")
    print("╠════════════╬════════╣")

    for subject, marks in data.items():
        print(f"║ {subject:<10} ║ {marks:6.2f} ║")

    print("╚════════════╩════════╝")

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
print("**************************************************")

# No.3: Top student in each subject
print_top_student(data_hash)
print("**************************************************")

# No.4: Average marks in each subject
uniq_subject = get_subject(data_hash)
calculate_avg_mark(uniq_subject, data_hash)
print("**************************************************")

# No. 5: Total marks for each student
print_total_mark(total_mark_hash)
print("**************************************************")

# No.6 & No.7 Update the marks of a given student in a given subject & append the new student marks to the database
'''
update_or_append(database_file, "Somu", "Maths", "99")
update_or_append(database_file, "Somu", "Science", "89")
update_or_append(database_file, "Somu", "Social", "49")
'''

# No.8: Remove existing student from the database
'''
remove_data(database_file, "Somu")
'''

# No.9: Progress card for each student
print("\nPrinting progress cards for all students:")
for student, subjects in data_hash.items():
    print_prog_card(student, subjects)