import csv
import re

# Read movie records from CSV file
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    movies = list(reader)

# Display all movie information
print("----- All Movie Information -----")

for movie in movies:
    print(movie)

# Search movie using Movie ID
movie_id = input("\nEnter Movie ID to search: ")

found = False

for movie in movies:
    if movie["Movie ID"] == movie_id:
        print("\n----- Movie Found -----")
        for key, value in movie.items():
            print(key + ":", value)
        found = True
        break

if not found:
    print("Movie not found.")

# Search movies by title using Regular Expression
pattern = input("\nEnter title or part of title to search: ")

print("\n----- Movies Matching Title -----")

found = False

for movie in movies:
    if re.search(pattern, movie["Title"], re.IGNORECASE):
        print(movie)
        found = True

if not found:
    print("No matching movies found.")
