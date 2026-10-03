import csv
import json

# Read data from CSV file
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Convert CSV data into a list of dictionaries
    data = list(csv_reader)

# Store data in JSON file
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON!")


//input
Name,Age,Course,Marks
Ishita,19,CSE,85
Rahul,20,CSE,78
Sneha,19,AI,92
//output
[
    {
        "Name": "Ishita",
        "Age": "19",
        "Course": "CSE",
        "Marks": "85"
    },
    {
        "Name": "Rahul",
        "Age": "20",
        "Course": "CSE",
        "Marks": "78"
    },
    {
        "Name": "Sneha",
        "Age": "19",
        "Course": "AI",
        "Marks": "92"
    }
]
