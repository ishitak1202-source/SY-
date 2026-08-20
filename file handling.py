filename = "demo.txt"

# Create a new file using write mode.
# If the file already exists, its old contents will be replaced.
file = open(filename, "w")
file.write("Hello, this is line one.\n")
file.write("Welcome to file handling in Python.\n")
file.close()

print("File created and written successfully.\n")

# Open the file in read mode and display its contents.
file = open(filename, "r")
data = file.read()
file.close()

print("Contents before adding new data:\n")
print(data)

# Open the file in append mode.
# The existing contents remain unchanged and new data is added at the end.
file = open(filename, "a")
file.write("This is an additional line.\n")
file.close()

print("New content added successfully.\n")

# Read the file again to check the updated contents.
file = open(filename, "r")
data = file.read()
file.close()

print("Contents after appending:\n")
print(data)

