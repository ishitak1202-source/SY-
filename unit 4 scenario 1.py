import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create NumPy array of treatment costs
costs = np.array([15000, 25000, 18000, 35000, 12000,
                  45000, 22000, 30000, 10000, 28000])

# Calculate mean, maximum and minimum
print("Treatment Costs:")
print(costs)

print("\nAverage Treatment Cost:")
print(np.mean(costs))

print("\nMaximum Treatment Cost:")
print(np.max(costs))

print("\nMinimum Treatment Cost:")
print(np.min(costs))

# Create Pandas DataFrame
df = pd.DataFrame({
    "PatientID": [101, 102, 103, 104, 105,
                  106, 107, 108, 109, 110],
    "TreatmentCost": costs
})

print("\nHospital Treatment Data:")
print(df)

# Display patients whose treatment cost exceeds 20000
print("\nPatients with Treatment Cost Above 20000:")
print(df[df["TreatmentCost"] > 20000])

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate total treatment cost
print("\nTotal Treatment Cost:")
print(np.sum(costs))

# Calculate number of patients
print("\nTotal Number of Patients:")
print(len(df))

# Treatment cost distribution
plt.bar(df["PatientID"], df["TreatmentCost"])

plt.title("Hospital Treatment Cost Analysis")
plt.xlabel("Patient ID")
plt.ylabel("Treatment Cost")
plt.show()

# Histogram of treatment costs
plt.hist(df["TreatmentCost"], bins=5)

plt.title("Treatment Cost Distribution")
plt.xlabel("Treatment Cost")
plt.ylabel("Number of Patients")
plt.show()

# Box plot
df.boxplot(column="TreatmentCost")

plt.title("Treatment Cost Box Plot")
plt.ylabel("Treatment Cost")
plt.show()
