# nutrition_tracker.py
# Practical 8 Part 2: Nutrition Data Tracker

class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_total(food_items):
    total_cal = sum(item.calories for item in food_items)
    total_pro = sum(item.protein for item in food_items)
    total_carb = sum(item.carbs for item in food_items)
    total_fat = sum(item.fat for item in food_items)

    if total_cal > 2500:
        print("Warning: Total calories exceed 2500 kcal!")
    if total_fat > 90:
        print("Warning: Total fat exceeds 90 g!")

    return total_cal, total_pro, total_carb, total_fat

# Example usage (required)
if __name__ == "__main__":
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    banana = food_item("Banana", 105, 1.3, 27, 0.4)
    chicken = food_item("Chicken Breast", 165, 31, 0, 3.6)
    daily = [apple, banana, chicken]
    cal, pro, carb, fat = calculate_total(daily)

    print("\n=== Daily Nutrition Summary ===")
    print(f"Total calories:  {cal:.1f} kcal")
    print(f"Total protein:   {pro:.1f} g")
    print(f"Total carbohydrates: {carb:.1f} g")
    print(f"Total fat:       {fat:.1f} g")
