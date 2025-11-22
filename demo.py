#!/usr/bin/env python3
"""Demo script for Recipe Generator and Meal Planner

This script demonstrates the key features of the application without user interaction.
"""

from datetime import datetime
from recipe_generator import RecipeGenerator
from meal_planner import MealPlanner


def main():
    """Run the demo."""
    print("=" * 70)
    print("RECIPE GENERATOR AND MEAL PLANNER DEMO")
    print("=" * 70)
    
    # Initialize
    generator = RecipeGenerator()
    planner = MealPlanner(generator)
    
    # Demo 1: Show all recipes
    print("\n1. ALL AVAILABLE RECIPES")
    print("-" * 70)
    recipes = generator.get_all_recipes()
    print(f"Total recipes: {len(recipes)}\n")
    for recipe in recipes:
        print(f"  • {recipe.name} ({recipe.category})")
    
    # Demo 2: Show a specific recipe
    print("\n\n2. RECIPE DETAILS: Spaghetti Carbonara")
    print("-" * 70)
    for recipe in recipes:
        if recipe.name == "Spaghetti Carbonara":
            print(recipe)
            break
    
    # Demo 3: Search recipes
    print("\n3. SEARCH RESULTS: 'chicken'")
    print("-" * 70)
    results = generator.search_recipes("chicken")
    print(f"Found {len(results)} recipe(s):")
    for recipe in results:
        print(f"  • {recipe.name}")
    
    # Demo 4: Get recipes by category
    print("\n\n4. BREAKFAST RECIPES")
    print("-" * 70)
    breakfast = generator.get_recipes_by_category("breakfast")
    for recipe in breakfast:
        print(f"  • {recipe.name} - {recipe.prep_time + recipe.cook_time} min total")
    
    # Demo 5: Create weekly meal plan
    print("\n\n5. WEEKLY MEAL PLAN")
    print("-" * 70)
    start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    planner.create_weekly_plan(
        start_date=start_date,
        include_breakfast=True,
        include_lunch=True,
        include_dinner=True,
        include_snack=False
    )
    planner.print_weekly_plan()
    
    # Demo 6: Generate shopping list
    print("\n\n6. SHOPPING LIST")
    print("-" * 70)
    shopping_list = planner.get_shopping_list()
    print(f"Shopping list contains ingredients for {len(shopping_list)} recipes:\n")
    for recipe_name in list(shopping_list.keys())[:3]:  # Show first 3 recipes
        print(f"{recipe_name}:")
        for ingredient in shopping_list[recipe_name]:
            print(f"  - {ingredient}")
        print()
    
    if len(shopping_list) > 3:
        print(f"... and {len(shopping_list) - 3} more recipes")
    
    print("\n" + "=" * 70)
    print("END OF DEMO")
    print("=" * 70)
    print("\nTo try the interactive version, run: python3 main.py")


if __name__ == "__main__":
    main()
