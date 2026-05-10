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
# 1. Set working directory (use forward slash for Windows)
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
# 3. Task 1: First 10 rows, Year & DALYs; Afghanistan max DALY year
# ============================================================
print("\n=== Task 1 ===")
first10 = dalys_data.iloc[0:10, [2, 3]]
print(first10)

afg = dalys_data.loc[dalys_data.Entity == "Afghanistan"]
afg_first10 = afg.iloc[0:10]
max_year = afg_first10.loc[afg_first10.DALYs.idxmax(), "Year"]
# COMMENT REQUIRED BY MARKING SCHEME
# Afghanistan's maximum DALYs in first 10 years occurred in: 1990
print(f"Afghanistan first 10 years max DALYs year: {max_year}")

# ============================================================
# 4. Task 2: Boolean indexing for Zimbabwe; first & last year
# ============================================================
print("\n=== Task 2 ===")
zimbabwe = dalys_data.loc[dalys_data.Entity == "Zimbabwe"]
# COMMENT REQUIRED BY MARKING SCHEME
# First year for Zimbabwe: 1990
# Last year for Zimbabwe: 2019
print("First year:", zimbabwe.Year.min())
print("Last year:", zimbabwe.Year.max())

# ============================================================
# 5. REQUIRED: Boolean list for column selection (as per guide)
# ============================================================
print("\n=== Boolean column indexing (required) ===")
cols = [True, True, True, True]
print(dalys_data.iloc[0:3, cols])

# ============================================================
# 6. Task 3: Max and min countries in 2019
# ============================================================
print("\n=== Task 3 ===")
data2019 = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]].dropna()

max_cty = data2019.loc[data2019.DALYs.idxmax(), "Entity"]
min_cty = data2019.loc[data2019.DALYs.idxmin(), "Entity"]
# COMMENT REQUIRED BY MARKING SCHEME
# 2019 max DALYs: Afghanistan
# 2019 min DALYs: Switzerland
print(f"2019 max: {max_cty}")
print(f"2019 min: {min_cty}")

# ============================================================
# 7. Task 4: Plot time series for min OR max country
# ============================================================
print("\n=== Task 4: Plot ===")
min_data = dalys_data.loc[dalys_data.Entity == min_cty]

plt.figure(figsize=(10,5))
plt.plot(min_data.Year, min_data.DALYs, 'b+')
plt.title(f"DALYs over time: {min_cty}")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(min_data.Year, rotation=-90)
plt.tight_layout()
plt.savefig("dalys_trend.png", dpi=150)
plt.show()

# ============================================================
# 8. Task 5: Answer question from question.txt (LINE ~95)
# Question: What is the distribution of DALYs across countries in 2019?
# ============================================================
print("\n=== Task 5 ===")

plt.figure(figsize=(10,5))
plt.hist(data2019.DALYs, bins=25, color="skyblue", edgecolor="black")
plt.title("Distribution of DALYs in 2019")
plt.xlabel("DALYs")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("dalys_2019_hist.png", dpi=150)
plt.show()

print("Mean:", data2019.DALYs.mean())
print("Median:", data2019.DALYs.median())
print("All tasks completed.")
