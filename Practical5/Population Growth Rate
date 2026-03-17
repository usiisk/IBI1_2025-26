print("\n" + "=" * 50)
print("3. Population Growth Rate")
print("=" * 50)

# Data: country -> (pop2020, pop2024) in millions
population_data = {
    "UK": (66.7, 69.2),
    "China": (1426, 1410),
    "Italy": (59.4, 58.9),
    "Brazil": (208.6, 212.0),
    "USA": (331.6, 340.1)
}

# Calculate percent change for each country
percent_changes = {}
for country, (pop2020, pop2024) in population_data.items():
    change = ((pop2024 - pop2020) / pop2020) * 100
    percent_changes[country] = change
    print(f"{country}: {change:.2f}%")

# Sort by percent change descending (largest increase to largest decrease)
sorted_changes = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)

print("\nPopulation changes (largest increase to largest decrease):")
for country, change in sorted_changes:
    print(f"  {country}: {change:.2f}%")

# Identify countries with largest increase and largest decrease
largest_increase_country = sorted_changes[0][0]
largest_increase_value = sorted_changes[0][1]
largest_decrease_country = sorted_changes[-1][0]
largest_decrease_value = sorted_changes[-1][1]

print(f"\nLargest increase: {largest_increase_country} ({largest_increase_value:.2f}%)")
print(f"Largest decrease: {largest_decrease_country} ({largest_decrease_value:.2f}%)")

# Bar chart of population changes
plt.figure(figsize=(8, 5))
countries = [item[0] for item in sorted_changes]  # order from largest to smallest
changes = [item[1] for item in sorted_changes]
colors = ['green' if c > 0 else 'red' for c in changes]  # green for increase, red for decrease
plt.bar(countries, changes, color=colors)
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.title("Population Change from 2020 to 2024")
plt.axhline(y=0, color='black', linewidth=0.8)  # horizontal line at zero
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\nAll tasks completed.")
