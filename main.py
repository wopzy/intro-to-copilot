#!/usr/bin/env python3
"""Main program for Recipe Generator and Meal Planner

This program demonstrates the recipe generator and meal planner functionality.
"""

import sys
from datetime import datetime
from recipe_generator import RecipeGenerator
from meal_planner import MealPlanner


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("RECIPE GENERATOR AND MEAL PLANNER")
    print("=" * 60)
    print("1. View all recipes")
    print("2. View recipes by category")
    print("3. Get a random recipe")
    print("4. Search recipes by keyword")
    print("5. Create weekly meal plan")
    print("6. View current meal plan")
    print("7. Generate shopping list")
    print("8. View specific recipe details")
    print("9. Exit")
    print("=" * 60)


def view_all_recipes(generator):
    """Display all available recipes."""
    recipes = generator.get_all_recipes()
    print(f"\nTotal recipes available: {len(recipes)}")
    print("\nRecipes by category:")
    
    categories = {}
    for recipe in recipes:
        if recipe.category not in categories:
            categories[recipe.category] = []
        categories[recipe.category].append(recipe.name)
    
    for category, recipe_names in sorted(categories.items()):
        print(f"\n{category.upper()}:")
        for name in recipe_names:
            print(f"  - {name}")


def view_recipes_by_category(generator):
    """Display recipes filtered by category."""
    print("\nCategories: breakfast, lunch, dinner, snack")
    category = input("Enter category: ").strip()
    
    recipes = generator.get_recipes_by_category(category)
    
    if recipes:
        print(f"\n{category.upper()} Recipes:")
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe.name}")
    else:
        print(f"No recipes found for category: {category}")


def get_random_recipe(generator):
    """Display a random recipe."""
    print("\nPress Enter for any category, or specify: breakfast, lunch, dinner, snack")
    category = input("Enter category (or press Enter): ").strip()
    
    try:
        if category:
            recipe = generator.get_random_recipe(category)
        else:
            recipe = generator.get_random_recipe()
        
        print(recipe)
    except ValueError as e:
        print(f"Error: {e}")


def search_recipes(generator):
    """Search for recipes by keyword."""
    keyword = input("\nEnter search keyword: ").strip()
    
    if not keyword:
        print("Please enter a keyword to search.")
        return
    
    recipes = generator.search_recipes(keyword)
    
    if recipes:
        print(f"\nFound {len(recipes)} recipe(s) matching '{keyword}':")
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe.name}")
    else:
        print(f"No recipes found matching '{keyword}'")


def create_weekly_plan(planner):
    """Create a new weekly meal plan."""
    print("\nCreate Weekly Meal Plan")
    print("Include meals? (y/n)")
    
    include_breakfast = input("Breakfast (y/n): ").strip().lower() == 'y'
    include_lunch = input("Lunch (y/n): ").strip().lower() == 'y'
    include_dinner = input("Dinner (y/n): ").strip().lower() == 'y'
    include_snack = input("Snack (y/n): ").strip().lower() == 'y'
    
    print("\nGenerating meal plan...")
    planner.create_weekly_plan(
        include_breakfast=include_breakfast,
        include_lunch=include_lunch,
        include_dinner=include_dinner,
        include_snack=include_snack
    )
    
    print("Meal plan created successfully!")
    planner.print_weekly_plan()


def view_meal_plan(planner):
    """Display the current meal plan."""
    planner.print_weekly_plan()


def generate_shopping_list(planner):
    """Generate and display shopping list."""
    planner.print_shopping_list()


def view_recipe_details(generator):
    """Display detailed information about a specific recipe."""
    view_all_recipes(generator)
    
    recipe_name = input("\nEnter recipe name: ").strip()
    
    recipes = generator.get_all_recipes()
    for recipe in recipes:
        if recipe.name.lower() == recipe_name.lower():
            print(recipe)
            return
    
    print(f"Recipe '{recipe_name}' not found.")


def main():
    """Main program loop."""
    generator = RecipeGenerator()
    planner = MealPlanner(generator)
    
    print("\nWelcome to Recipe Generator and Meal Planner!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            view_all_recipes(generator)
        elif choice == '2':
            view_recipes_by_category(generator)
        elif choice == '3':
            get_random_recipe(generator)
        elif choice == '4':
            search_recipes(generator)
        elif choice == '5':
            create_weekly_plan(planner)
        elif choice == '6':
            view_meal_plan(planner)
        elif choice == '7':
            generate_shopping_list(planner)
        elif choice == '8':
            view_recipe_details(generator)
        elif choice == '9':
            print("\nThank you for using Recipe Generator and Meal Planner!")
            print("Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
