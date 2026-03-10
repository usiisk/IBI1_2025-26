# Store variables
age = 70
weight = 70
cr = 80
gender = "male"

# Check each condition
if age >= 100:
    print("Error: age must be < 100")
elif weight <= 20 or weight >= 80:
    print("Error: weight must be >20 and <80 kg")
elif cr <= 0 or cr >= 100:
    print("Error: creatine must be >0 and <100 μmol/l")
elif gender not in ["male", "female"]:
    print("Error: gender must be 'male' or 'female'")
else:
    # Calculate
    crcl = ((140 - age) * weight) / (72 * cr)
    if gender == "female":
        crcl = crcl * 0.85
    print("Creatine clearance =", crcl)
