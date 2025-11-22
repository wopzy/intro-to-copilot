# Recipe Generator and Meal Planner

A Python application for generating recipes and planning weekly meals.

## Features

- **Recipe Generator**: Browse through a collection of 8 delicious recipes across different categories
- **Meal Planner**: Create customized weekly meal plans
- **Shopping List**: Automatically generate shopping lists for your meal plans
- **Recipe Search**: Search recipes by name or ingredient
- **Recipe Details**: View detailed information including ingredients, instructions, prep time, and cook time

## Recipe Categories

- Breakfast
- Lunch
- Dinner
- Snack

## Available Recipes

- Classic Pancakes
- Berry Smoothie
- Chicken Stir Fry
- Spaghetti Carbonara
- Greek Salad
- Vegetable Soup
- Grilled Cheese Sandwich
- Chocolate Chip Cookies

## Installation

No additional dependencies required! This application uses only Python standard library.

Requirements:
- Python 3.6 or higher

## Usage

### Quick Demo

To see a quick demonstration of all features without user interaction:

```bash
python3 demo.py
```

This will show:
- All available recipes
- Recipe details
- Search functionality
- Recipes by category
- Weekly meal plan generation
- Shopping list creation

### Running the Main Application

```bash
python3 main.py
```

This will start an interactive menu where you can:
1. View all recipes
2. View recipes by category
3. Get a random recipe
4. Search recipes by keyword
5. Create weekly meal plan
6. View current meal plan
7. Generate shopping list
8. View specific recipe details
9. Exit

### Running Tests

To run the recipe generator tests:
```bash
python3 test_recipe_generator.py
```

To run the meal planner tests:
```bash
python3 test_meal_planner.py
```

## Module Documentation

### recipe_generator.py

Contains the `Recipe` and `RecipeGenerator` classes:
- `Recipe`: Represents a recipe with name, ingredients, instructions, prep time, cook time, servings, and category
- `RecipeGenerator`: Manages a collection of recipes and provides methods to search and filter them

### meal_planner.py

Contains the `MealPlan` and `MealPlanner` classes:
- `MealPlan`: Represents a meal plan for a specific day
- `MealPlanner`: Creates weekly meal plans and generates shopping lists

## Example Usage

### Creating a Weekly Meal Plan

```python
from recipe_generator import RecipeGenerator
from meal_planner import MealPlanner

generator = RecipeGenerator()
planner = MealPlanner(generator)

# Create a weekly plan with breakfast, lunch, and dinner
plans = planner.create_weekly_plan(
    include_breakfast=True,
    include_lunch=True,
    include_dinner=True,
    include_snack=False
)

# Print the meal plan
planner.print_weekly_plan()

# Generate shopping list
planner.print_shopping_list()
```

### Searching for Recipes

```python
from recipe_generator import RecipeGenerator

generator = RecipeGenerator()

# Search by keyword
recipes = generator.search_recipes("chicken")

# Get recipes by category
breakfast_recipes = generator.get_recipes_by_category("breakfast")

# Get a random recipe
random_recipe = generator.get_random_recipe()
```

## Contributing

Feel free to add more recipes by editing the `_load_recipes()` method in the `RecipeGenerator` class!

## License

This project is open source and available under the MIT License.
