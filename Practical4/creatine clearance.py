# ==============================================
# Creatine Clearance Calculator (Cockcroft-Gault)
# Pseudocode:
# 1. Define input variables: age, weight, cr, gender
# 2. Check if inputs are within valid ranges
# 3. If any input invalid, print which one needs correction
# 4. If all valid, calculate CrCl
# 5. Apply 0.85 factor if female
# 6. Print the final result with unit
# ==============================================

# Input variables
age = 70
weight = 70
cr = 80
gender = "male"

# Flag to track input validity
valid = True

# Check input ranges one by one
if age >= 100:
    print("Error: age must be < 100")
    valid = False
if weight <= 20 or weight >= 80:
    print("Error: weight must be >20 and <80 kg")
    valid = False
if cr <= 0 or cr >= 100:
    print("Error: creatine must be >0 and <100 μmol/l")
    valid = False
if gender not in ["male", "female"]:
    print("Error: gender must be 'male' or 'female'")
    valid = False

# Calculate only if all inputs are valid
if valid:
    crcl = ((140 - age) * weight) / (72 * cr)
    if gender == "female":
        crcl = crcl * 0.85
    print(f"Creatine clearance (CrCl) = {crcl:.2f} mL/min")
