class FoodItem:
    """
    Represents a food item with its nutritional values.
    """
    def __init__(self, name, calories, protein, carbs, fat):
        """
        Initialize a food item.

        Args:
            name (str): Name of the food.
            calories (float): Energy in kcal.
            protein (float): Protein in grams.
            carbs (float): Carbohydrates in grams.
            fat (float): Fat in grams.
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def __repr__(self):
        return f"FoodItem('{self.name}', {self.calories}, {self.protein}, {self.carbs}, {self.fat})"


def calculate_total(food_items):
    """
    Calculate total nutritional intake from a list of FoodItem objects.
    Prints warnings if calories > 2500 or fat > 90 g.

    Args:
        food_items (list of FoodItem): Items consumed over 24 hours.

    Returns:
        tuple: (total_calories, total_protein, total_carbs, total_fat)
    """
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    for item in food_items:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    # Warnings
    if total_calories > 2500:
        print(f" Warning: Total calories ({total_calories:.1f} kcal) exceed 2500 kcal.")
    if total_fat > 90:
        print(f" Warning: Total fat ({total_fat:.1f} g) exceeds 90 g.")

    return total_calories, total_protein, total_carbs, total_fat


# Example usage
if __name__ == "__main__":
    # Create food items
    apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
    banana = FoodItem("Banana", 105, 1.3, 27, 0.4)
    chicken_breast = FoodItem("Chicken Breast", 165, 31, 0, 3.6)
    rice = FoodItem("Rice (1 cup)", 206, 4.3, 45, 0.4)
    burger = FoodItem("Cheeseburger", 550, 30, 45, 35)
    fries = FoodItem("French Fries", 365, 4, 48, 17)

    # Daily intake list (modify to test warnings)
    daily_intake = [apple, banana, chicken_breast, rice, burger, fries]

    # Calculate totals
    cal, prot, carb, fat = calculate_total(daily_intake)

    # Print summary
    print("\n=== Daily Nutrition Summary ===")
    print(f"Total calories:  {cal:.1f} kcal")
    print(f"Total protein:   {prot:.1f} g")
    print(f"Total carbs:     {carb:.1f} g")
    print(f"Total fat:       {fat:.1f} g")
