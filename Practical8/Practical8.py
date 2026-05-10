# ==================== Part 1: Protein mass predictor ====================

# Monoisotopic residue masses (amu)
residue_masses = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

def protein_mass(sequence):
    """
    Calculate the total mass of a protein sequence in amu.
    Raises a KeyError if an unknown amino acid is encountered.
    """
    mass = 0.0
    for aa in sequence.upper():
        if aa not in residue_masses:
            raise ValueError(f"Unknown amino acid: '{aa}'")
        mass += residue_masses[aa]
    return mass

# Example function call (as required)
if __name__ == "__main__":
    example_seq = "ACDEFGHIKLMNPQRSTVWY"
    try:
        mass = protein_mass(example_seq)
        print(f"Example protein mass: {mass:.2f} amu")
    except ValueError as e:
        print(f"Error: {e}")

# ==================== Part 2: Nutrition Data Tracker ====================

class food_item:
    """Class to store nutritional information for a food item."""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories    # kcal
        self.protein = protein      # grams
        self.carbs = carbs          # grams
        self.fat = fat              # grams

def calculate_total(food_items):
    """
    Calculate total nutritional intake from a list of food_item objects.
    Prints warnings if calories exceed 2500 or fat exceeds 90 g.
    Returns totals as a tuple (calories, protein, carbs, fat).
    """
    total_cal = sum(item.calories for item in food_items)
    total_pro = sum(item.protein for item in food_items)
    total_carb = sum(item.carbs for item in food_items)
    total_fat = sum(item.fat for item in food_items)
    
    # Warnings
    if total_cal > 2500:
        print("Warning: Total calories exceed 2500 kcal!")
    if total_fat > 90:
        print("Warning: Total fat exceed 90 g!")
    
    return total_cal, total_pro, total_carb, total_fat

# Example usage (must be present in the script)
if __name__ == "__main__":
    # Create food items
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    banana = food_item("Banana", 105, 1.3, 27, 0.4)
    chicken_breast = food_item("Chicken Breast", 165, 31, 0, 3.6)
    rice = food_item("Rice (1 cup)", 206, 4.3, 45, 0.4)
    burger = food_item("Cheeseburger", 550, 30, 45, 35)
    fries = food_item("French Fries", 365, 4, 48, 17)
    
    # List of consumed items over 24 hours
    daily_intake = [apple, banana, chicken_breast, rice, burger, fries]
    
    # Calculate totals
    cal, prot, carb, fat = calculate_total(daily_intake)
    
    # Print summary
    print("\n=== Daily Nutrition Summary ===")
    print(f"Total calories:  {cal:.1f} kcal")
    print(f"Total protein:   {prot:.1f} g")
    print(f"Total carbohydrates: {carb:.1f} g")
    print(f"Total fat:       {fat:.1f} g")
