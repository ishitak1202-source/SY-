# Open the input file in read mode
file = open("input.txt", "r")

# Read all lines
lines = file.readlines()

# Close the file
file.close()

# Count total number of lines
print("Total number of lines:", len(lines))

# Extract first two lines
first_two_lines = lines[:2]

# Display first two lines
print("First two lines:")
for line in first_two_lines:
    print(line, end="")

# Write first two lines into a new file
output_file = open("output.txt", "w")

for line in first_two_lines:
    output_file.write(line)

output_file.close()

print("\nFirst two lines have been written to output.txt")
