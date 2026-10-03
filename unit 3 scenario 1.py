import csv
import sys

# Check if filename is provided
if len(sys.argv) != 2:
    print("Usage: python employee.py <filename>")
    sys.exit()

filename = sys.argv[1]

try:
    # Open and read the CSV file
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        employees = list(reader)

    # Display all employee details
    print("\n--- All Employee Details ---")

    for employee in employees:
        print(employee)

    # Search employee by ID
    emp_id = input("\nEnter Employee ID to search: ")

    found = False

    for employee in employees:
        if employee["Employee ID"] == emp_id:
            print("\n--- Employee Found ---")
            for key, value in employee.items():
                print(key + ":", value)
            found = True
            break

    if not found:
        print("Employee not found.")

except FileNotFoundError:
    print("File not found.")
