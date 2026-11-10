import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("student.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

df["StudyHours"] = df["StudyHours"].fillna(
    df["StudyHours"].median()
)

df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].median()
)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].median()
)

df["Gender"] = df["Gender"].fillna(
    df["Gender"].mode()[0]
)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Maximum marks
print("\nMaximum Marks:")
print(df["Marks"].max())

# Minimum marks
print("\nMinimum Marks:")
print(df["Marks"].min())

# Average marks by gender
print("\nAverage Marks by Gender:")
print(df.groupby("Gender")["Marks"].mean())

# Average marks by attendance
print("\nAverage Marks by Attendance:")
print(df.groupby("Attendance")["Marks"].mean())

# Average study hours
print("\nAverage Study Hours:")
print(df["StudyHours"].mean())

# Gender distribution
print("\nGender Count:")
print(df["Gender"].value_counts())

# Gender percentage
print("\nGender Percentage:")
print(df["Gender"].value_counts(normalize=True) * 100)

# Bar graph - Gender distribution
df["Gender"].value_counts().plot(kind="bar")

plt.title("Student Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.show()

# Scatter plot - Study Hours vs Marks
plt.scatter(df["StudyHours"], df["Marks"])

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Histogram - Marks distribution
plt.hist(df["Marks"], bins=5)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# Box plot - Marks by Gender
df.boxplot(column="Marks", by="Gender")

plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Marks")
plt.show()

# Scatter plot - Attendance vs Marks
plt.scatter(df["Attendance"], df["Marks"])

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

# Box plot - Study Hours
df.boxplot(column="StudyHours")

plt.title("Study Hours Distribution")
plt.ylabel("Study Hours")
plt.show()

# Correlation between numerical columns
print("\nCorrelation Matrix:")
print(df.select_dtypes(include=np.number).corr())
