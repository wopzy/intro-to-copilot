"""Recipe Generator Module

This module provides functionality to generate recipes with ingredients and instructions.
"""

import random
from typing import List, Dict


class Recipe:
    """Represents a recipe with name, ingredients, and instructions."""
    
    def __init__(self, name: str, ingredients: List[str], instructions: List[str], 
                 prep_time: int, cook_time: int, servings: int, category: str):
        """
        Initialize a Recipe.
        
        Args:
            name: Name of the recipe
            ingredients: List of ingredients needed
            instructions: Step-by-step cooking instructions
            prep_time: Preparation time in minutes
            cook_time: Cooking time in minutes
            servings: Number of servings
            category: Recipe category (breakfast, lunch, dinner, snack)
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.category = category
    
    def __str__(self) -> str:
        """Return a formatted string representation of the recipe."""
        ingredients_str = "\n  - ".join(self.ingredients)
        instructions_str = "\n  ".join([f"{i+1}. {step}" for i, step in enumerate(self.instructions)])
        
        return f"""
{self.name}
{'=' * len(self.name)}
Category: {self.category.capitalize()}
Prep Time: {self.prep_time} minutes
Cook Time: {self.cook_time} minutes
Total Time: {self.prep_time + self.cook_time} minutes
Servings: {self.servings}

Ingredients:
  - {ingredients_str}

Instructions:
  {instructions_str}
"""


class RecipeGenerator:
    """Generates recipes from a predefined collection."""
    
    def __init__(self):
        """Initialize the recipe generator with sample recipes."""
        self.recipes = self._load_recipes()
    
    def _load_recipes(self) -> List[Recipe]:
        """Load sample recipes into the generator."""
        return [
            Recipe(
                name="Classic Pancakes",
                ingredients=[
                    "1 1/2 cups all-purpose flour",
                    "3 1/2 teaspoons baking powder",
                    "1 tablespoon white sugar",
                    "1/4 teaspoon salt",
                    "1 1/4 cups milk",
                    "1 egg",
                    "3 tablespoons butter, melted"
                ],
                instructions=[
                    "Sift together flour, baking powder, sugar, and salt",
                    "Make a well in the center and pour in milk, egg, and melted butter",
                    "Mix until smooth",
                    "Heat a lightly oiled griddle over medium-high heat",
                    "Pour batter onto the griddle and cook until bubbles form",
                    "Flip and cook until golden brown"
                ],
                prep_time=5,
                cook_time=15,
                servings=4,
                category="breakfast"
            ),
            Recipe(
                name="Chicken Stir Fry",
                ingredients=[
                    "2 chicken breasts, sliced",
                    "2 cups mixed vegetables (bell peppers, broccoli, carrots)",
                    "3 tablespoons soy sauce",
                    "2 tablespoons vegetable oil",
                    "2 cloves garlic, minced",
                    "1 teaspoon ginger, grated",
                    "1 tablespoon cornstarch",
                    "Cooked rice for serving"
                ],
                instructions=[
                    "Heat oil in a large wok or skillet over high heat",
                    "Add chicken and cook until no longer pink",
                    "Add garlic and ginger, cook for 30 seconds",
                    "Add vegetables and stir-fry for 3-4 minutes",
                    "Mix soy sauce with cornstarch and add to the wok",
                    "Stir until sauce thickens",
                    "Serve over rice"
                ],
                prep_time=15,
                cook_time=15,
                servings=4,
                category="dinner"
            ),
            Recipe(
                name="Greek Salad",
                ingredients=[
                    "4 tomatoes, cut into wedges",
                    "1 cucumber, sliced",
                    "1 red onion, thinly sliced",
                    "1 cup Kalamata olives",
                    "200g feta cheese, cubed",
                    "1/4 cup olive oil",
                    "2 tablespoons red wine vinegar",
                    "1 teaspoon dried oregano",
                    "Salt and pepper to taste"
                ],
                instructions=[
                    "Combine tomatoes, cucumber, onion, and olives in a large bowl",
                    "Whisk together olive oil, vinegar, oregano, salt, and pepper",
                    "Pour dressing over vegetables and toss gently",
                    "Top with feta cheese",
                    "Serve immediately or chill for 30 minutes"
                ],
                prep_time=15,
                cook_time=0,
                servings=4,
                category="lunch"
            ),
            Recipe(
                name="Spaghetti Carbonara",
                ingredients=[
                    "400g spaghetti",
                    "200g bacon or pancetta, diced",
                    "3 large eggs",
                    "1 cup Parmesan cheese, grated",
                    "2 cloves garlic, minced",
                    "Salt and black pepper to taste",
                    "Fresh parsley for garnish"
                ],
                instructions=[
                    "Cook spaghetti according to package directions",
                    "While pasta cooks, fry bacon until crispy",
                    "Add garlic to bacon and cook for 1 minute",
                    "Whisk eggs and Parmesan together in a bowl",
                    "Drain pasta, reserving 1 cup pasta water",
                    "Add hot pasta to bacon pan, remove from heat",
                    "Quickly stir in egg mixture, adding pasta water to create creamy sauce",
                    "Season with pepper and garnish with parsley"
                ],
                prep_time=10,
                cook_time=20,
                servings=4,
                category="dinner"
            ),
            Recipe(
                name="Berry Smoothie",
                ingredients=[
                    "1 cup mixed berries (strawberries, blueberries, raspberries)",
                    "1 banana",
                    "1 cup yogurt",
                    "1/2 cup milk",
                    "1 tablespoon honey",
                    "Ice cubes"
                ],
                instructions=[
                    "Add all ingredients to a blender",
                    "Blend until smooth and creamy",
                    "Add more milk if too thick",
                    "Pour into glasses and serve immediately"
                ],
                prep_time=5,
                cook_time=0,
                servings=2,
                category="breakfast"
            ),
            Recipe(
                name="Vegetable Soup",
                ingredients=[
                    "2 tablespoons olive oil",
                    "1 onion, diced",
                    "3 carrots, sliced",
                    "3 celery stalks, sliced",
                    "2 potatoes, cubed",
                    "4 cups vegetable broth",
                    "1 can diced tomatoes",
                    "2 cups green beans",
                    "2 teaspoons Italian seasoning",
                    "Salt and pepper to taste"
                ],
                instructions=[
                    "Heat olive oil in a large pot over medium heat",
                    "Sauté onion, carrots, and celery for 5 minutes",
                    "Add potatoes, broth, tomatoes, and seasoning",
                    "Bring to a boil, then reduce heat and simmer for 15 minutes",
                    "Add green beans and cook for 10 more minutes",
                    "Season with salt and pepper",
                    "Serve hot with crusty bread"
                ],
                prep_time=15,
                cook_time=30,
                servings=6,
                category="lunch"
            ),
            Recipe(
                name="Chocolate Chip Cookies",
                ingredients=[
                    "2 1/4 cups all-purpose flour",
                    "1 teaspoon baking soda",
                    "1 teaspoon salt",
                    "1 cup butter, softened",
                    "3/4 cup granulated sugar",
                    "3/4 cup brown sugar",
                    "2 large eggs",
                    "2 teaspoons vanilla extract",
                    "2 cups chocolate chips"
                ],
                instructions=[
                    "Preheat oven to 375°F (190°C)",
                    "Mix flour, baking soda, and salt in a bowl",
                    "Beat butter and both sugars until creamy",
                    "Add eggs and vanilla, beat well",
                    "Gradually blend in flour mixture",
                    "Stir in chocolate chips",
                    "Drop rounded tablespoons onto ungreased cookie sheets",
                    "Bake for 9-11 minutes until golden brown",
                    "Cool on baking sheet for 2 minutes, then transfer to wire rack"
                ],
                prep_time=15,
                cook_time=11,
                servings=48,
                category="snack"
            ),
            Recipe(
                name="Grilled Cheese Sandwich",
                ingredients=[
                    "2 slices bread",
                    "2 slices cheese (cheddar, Swiss, or American)",
                    "2 tablespoons butter"
                ],
                instructions=[
                    "Butter one side of each bread slice",
                    "Place one slice butter-side down in a skillet over medium heat",
                    "Add cheese slices on top",
                    "Top with second bread slice, butter-side up",
                    "Cook until golden brown, about 3-4 minutes",
                    "Flip and cook other side until golden and cheese is melted",
                    "Cut in half and serve hot"
                ],
                prep_time=5,
                cook_time=8,
                servings=1,
                category="lunch"
            )
        ]
    
    def get_all_recipes(self) -> List[Recipe]:
        """Return all available recipes."""
        return self.recipes
    
    def get_recipes_by_category(self, category: str) -> List[Recipe]:
        """
        Get recipes filtered by category.
        
        Args:
            category: Category to filter by (breakfast, lunch, dinner, snack)
            
        Returns:
            List of recipes in the specified category
        """
        return [r for r in self.recipes if r.category.lower() == category.lower()]
    
    def get_random_recipe(self, category: str = None) -> Recipe:
        """
        Get a random recipe, optionally filtered by category.
        
        Args:
            category: Optional category to filter by
            
        Returns:
            A random recipe
        """
        if category:
            recipes = self.get_recipes_by_category(category)
        else:
            recipes = self.recipes
        
        if not recipes:
            raise ValueError(f"No recipes found for category: {category}")
        
        return random.choice(recipes)
    
    def search_recipes(self, keyword: str) -> List[Recipe]:
        """
        Search recipes by keyword in name or ingredients.
        
        Args:
            keyword: Keyword to search for
            
        Returns:
            List of matching recipes
        """
        keyword_lower = keyword.lower()
        results = []
        
        for recipe in self.recipes:
            if keyword_lower in recipe.name.lower():
                results.append(recipe)
                continue
            
            for ingredient in recipe.ingredients:
                if keyword_lower in ingredient.lower():
                    results.append(recipe)
                    break
        
        return results
