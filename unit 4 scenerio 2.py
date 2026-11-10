import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create NumPy array of mobile prices
prices = np.array([15000, 25000, 18000, 35000, 42000,
                   55000, 28000, 65000, 12000, 45000])

# Calculate mean, median, maximum and minimum
print("Mobile Prices:")
print(prices)

print("\nAverage Mobile Price:")
print(np.mean(prices))

print("\nMedian Mobile Price:")
print(np.median(prices))

print("\nMaximum Mobile Price:")
print(np.max(prices))

print("\nMinimum Mobile Price:")
print(np.min(prices))

# Create Pandas DataFrame
df = pd.DataFrame({
    "MobileID": [101, 102, 103, 104, 105,
                 106, 107, 108, 109, 110],
    "MobilePrice": prices
})

print("\nMobile Data:")
print(df)

# Display mobiles costing more than 30000
print("\nMobiles Costing More Than 30000:")
print(df[df["MobilePrice"] > 30000])

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate total mobile price
print("\nTotal Mobile Price:")
print(np.sum(prices))

# Count total mobiles
print("\nTotal Number of Mobiles:")
print(len(df))

# Bar graph
plt.bar(df["MobileID"], df["MobilePrice"])

plt.title("Mobile Price Analysis")
plt.xlabel("Mobile ID")
plt.ylabel("Mobile Price")
plt.show()

# Histogram
plt.hist(df["MobilePrice"], bins=5)

plt.title("Mobile Price Distribution")
plt.xlabel("Mobile Price")
plt.ylabel("Frequency")
plt.show()

# Box plot
df.boxplot(column="MobilePrice")

plt.title("Mobile Price Box Plot")
plt.ylabel("Mobile Price")
plt.show()
