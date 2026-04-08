print("\n" + "=" * 50)
print("2. Heart Rate Analysis")
print("=" * 50)

# List of resting heart rates
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Number of patients and mean heart rate
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients
print(f"Number of patients: {num_patients}")
print(f"Mean heart rate: {mean_hr:.2f} bpm")

# Categorise heart rates
low = [hr for hr in heart_rates if hr < 60]
normal = [hr for hr in heart_rates if 60 <= hr <= 120]
high = [hr for hr in heart_rates if hr > 120]

count_low = len(low)
count_normal = len(normal)
count_high = len(high)

print(f"Low (<60 bpm): {count_low} patients")
print(f"Normal (60-120 bpm): {count_normal} patients")
print(f"High (>120 bpm): {count_high} patients")

# Find the largest category
categories = {"Low": count_low, "Normal": count_normal, "High": count_high}
largest_category = max(categories, key=categories.get)
print(f"The largest category is '{largest_category}' with {categories[largest_category]} patients.")

# Pie chart
plt.figure(figsize=(6, 6))
labels = ['Low (<60)', 'Normal (60-120)', 'High (>120)']
sizes = [count_low, count_normal, count_high]
colors = ['lightcoral', 'lightskyblue', 'gold']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Heart Rate Categories")
plt.axis('equal')
plt.show()
