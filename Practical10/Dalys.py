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
# 1. Set working directory
# ============================================================
os.chdir("C:/users/yjx34/desktop/IBI1")

print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# ============================================================
# 2. Load dataset
# ============================================================
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("\nFirst 5 rows:")
print(dalys_data.head(5))

print("\nDataset info:")
dalys_data.info()

print("\nStatistical summary:")
print(dalys_data.describe())

# ============================================================
# Task 1: First 10 rows, Year & DALYs; Afghanistan max DALY year
# ============================================================
print("\n=== Task 1 ===")
first10 = dalys_data.iloc[0:10, [2, 3]]
print(first10)

afg = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"]
afg_first10 = afg.iloc[0:10]
max_year = afg_first10.loc[afg_first10["DALYs"].idxmax(), "Year"]

print(f"Afghanistan first 10 years max DALYs year: {max_year}")

# ============================================================
# Task 2: Boolean indexing for Zimbabwe; first & last year
# ============================================================
print("\n=== Task 2 ===")
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("First year:", zimbabwe["Year"].min())
print("Last year:", zimbabwe["Year"].max())

# ============================================================
# REQUIRED: Boolean list for column selection
# ============================================================
print("\n=== Boolean column indexing ===")
cols = [True, True, True, True]
print(dalys_data.iloc[0:3, cols])

# ============================================================
# Task 3: Max and min countries in 2019
# ============================================================
print("\n=== Task 3 ===")
data2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]].dropna()

max_cty = data2019.loc[data2019["DALYs"].idxmax(), "Entity"]
min_cty = data2019.loc[data2019["DALYs"].idxmin(), "Entity"]

print(f"2019 max: {max_cty}")
print(f"2019 min: {min_cty}")

# ============================================================
# Task 4: Time series plot (LINE PLOT, not scatter)
# ============================================================
print("\n=== Task 4: Plot ===")
min_data = dalys_data.loc[dalys_data["Entity"] == min_cty]

plt.figure(figsize=(10,5))
plt.plot(min_data["Year"], min_data["DALYs"], 'b-', linewidth=2)  # FIXED: line instead of dots
plt.title(f"DALYs over time: {min_cty}", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs", fontsize=12)
plt.xticks(min_data["Year"], rotation=-90)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("dalys_trend.png", dpi=150)
plt.show()

# ============================================================
# Task 5: Histogram for 2019 DALYs distribution
# ============================================================
print("\n=== Task 5 ===")

plt.figure(figsize=(10,5))
plt.hist(data2019["DALYs"], bins=25, color="skyblue", edgecolor="black")
plt.title("Distribution of DALYs in 2019", fontsize=14)
plt.xlabel("DALYs", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("dalys_2019_hist.png", dpi=150)
plt.show()

print("Mean:", round(data2019["DALYs"].mean(), 2))
print("Median:", round(data2019["DALYs"].median(), 2))
print("All tasks completed successfully.")
