"""
IBI1 Practical 10: Global Disease Burden Analysis (DALYs)
Author: Student
Date: 2026-04-21
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. Set working directory (modify the path accordingly)
# ============================================================
os.chdir("\users\yjx34\desktop\IBI1")   

# Optional: verify current directory and file list
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# ============================================================
# 2. Load the dataset
# ============================================================
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Display first 5 rows (test)
print("\nFirst 5 rows of the dataset:")
print(dalys_data.head(5))

# Display data structure
print("\nDataset info:")
dalys_data.info()

# Statistical summary of numeric columns
print("\nStatistical summary:")
print(dalys_data.describe())

# ============================================================
# 3. Task 1: Show first 10 rows, columns Year (3rd) and DALYs (4th)
#    and find the year with maximum DALYs among Afghanistan's first 10 records
# ============================================================
print("\n=== Task 1: First 10 rows, columns Year & DALYs ===")
first10_years_dalys = dalys_data.iloc[0:10, [2, 3]]  # index 2 = Year, index 3 = DALYs
print(first10_years_dalys)

# Extract Afghanistan data, take first 10 rows
afghan_data = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"]
afghan_first10 = afghan_data.iloc[0:10]
max_dalys_year_afghan = afghan_first10.loc[afghan_first10["DALYs"].idxmax(), "Year"]
print(f"\nAfghanistan: Among the first 10 recorded years, the maximum DALYs occurred in {max_dalys_year_afghan}.")

# ============================================================
# 4. Task 2: Use boolean indexing to extract all years for Zimbabwe
#    and comment the first and last year
# ============================================================
print("\n=== Task 2: Zimbabwe data (all years) ===")
zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", :]
zimbabwe_years = zimbabwe_data["Year"]
print("Years for Zimbabwe:", zimbabwe_years.tolist())
print(f"First year recorded for Zimbabwe: {zimbabwe_years.min()}")
print(f"Last year recorded for Zimbabwe: {zimbabwe_years.max()}")

# ============================================================
# 5. Task 3: Find country with max and min DALYs in 2019
# ============================================================
print("\n=== Task 3: Countries with max and min DALYs in 2019 ===")
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
# Drop missing values if any
data_2019_clean = data_2019.dropna(subset=["DALYs"])

max_country = data_2019_clean.loc[data_2019_clean["DALYs"].idxmax(), "Entity"]
max_dalys = data_2019_clean["DALYs"].max()
min_country = data_2019_clean.loc[data_2019_clean["DALYs"].idxmin(), "Entity"]
min_dalys = data_2019_clean["DALYs"].min()

print(f"Country with highest DALYs in 2019: {max_country} ({max_dalys:.2f})")
print(f"Country with lowest DALYs in 2019: {min_country} ({min_dalys:.2f})")

# ============================================================
# 6. Task 4: Plot DALYs over time for one of the above countries
#    Here we plot for Zimbabwe (or you can change to max_country)
# ============================================================
print("\n=== Task 4: Plot DALYs over time for Zimbabwe ===")
plt.figure(figsize=(10, 5))
plt.plot(zimbabwe_data["Year"], zimbabwe_data["DALYs"], 'b-', marker='o', markersize=4)
plt.title("Disease Burden (DALYs) over Time in Zimbabwe", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs per 100,000", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("zimbabwe_dalys_trend.png", dpi=150)
plt.show()

# ============================================================
# 7. Task 5: Answer the question stated in question.txt
#    Question: Distribution of DALYs across all countries in 2019
#    Code start line number is indicated in question.txt (approx line 95)
# ============================================================
print("\n=== Task 5: Answering the question from question.txt ===")

# Extract 2019 DALYs values for all countries (already in data_2019_clean)
dalys_2019_values = data_2019_clean["DALYs"].dropna()

# Plot histogram
plt.figure(figsize=(10, 5))
plt.hist(dalys_2019_values, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Distribution of DALYs across All Countries in 2019", fontsize=14)
plt.xlabel("DALYs per 100,000", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("dalys_2019_distribution.png", dpi=150)
plt.show()

# Simple statistics
print("\n2019 DALYs statistics:")
print(f"  Mean: {dalys_2019_values.mean():.2f}")
print(f"  Median: {dalys_2019_values.median():.2f}")
print(f"  Std dev: {dalys_2019_values.std():.2f}")
print(f"  Min: {dalys_2019_values.min():.2f} ({min_country})")
print(f"  Max: {dalys_2019_values.max():.2f} ({max_country})")
print(f"  Number of countries: {len(dalys_2019_values)}")

# Optional: boxplot for further distribution insight
plt.figure(figsize=(6, 4))
plt.boxplot(dalys_2019_values, vert=True, patch_artist=True)
plt.title("Boxplot of DALYs in 2019")
plt.ylabel("DALYs per 100,000")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("dalys_2019_boxplot.png", dpi=150)
plt.show()

print("\nAll tasks completed. Check generated PNG files.")
