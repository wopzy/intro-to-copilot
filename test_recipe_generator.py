"""Unit tests for Recipe Generator module."""

import unittest
from recipe_generator import Recipe, RecipeGenerator


class TestRecipe(unittest.TestCase):
    """Test cases for the Recipe class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.recipe = Recipe(
            name="Test Recipe",
            ingredients=["ingredient1", "ingredient2"],
            instructions=["step1", "step2"],
            prep_time=10,
            cook_time=20,
            servings=4,
            category="lunch"
        )
    
    def test_recipe_creation(self):
        """Test that a recipe can be created with all attributes."""
        self.assertEqual(self.recipe.name, "Test Recipe")
        self.assertEqual(len(self.recipe.ingredients), 2)
        self.assertEqual(len(self.recipe.instructions), 2)
        self.assertEqual(self.recipe.prep_time, 10)
        self.assertEqual(self.recipe.cook_time, 20)
        self.assertEqual(self.recipe.servings, 4)
        self.assertEqual(self.recipe.category, "lunch")
    
    def test_recipe_str_representation(self):
        """Test the string representation of a recipe."""
        recipe_str = str(self.recipe)
        self.assertIn("Test Recipe", recipe_str)
        self.assertIn("ingredient1", recipe_str)
        self.assertIn("step1", recipe_str)
        self.assertIn("Prep Time: 10 minutes", recipe_str)


class TestRecipeGenerator(unittest.TestCase):
    """Test cases for the RecipeGenerator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.generator = RecipeGenerator()
    
    def test_generator_has_recipes(self):
        """Test that the generator loads recipes on initialization."""
        recipes = self.generator.get_all_recipes()
        self.assertGreater(len(recipes), 0)
    
    def test_get_all_recipes(self):
        """Test getting all recipes."""
        recipes = self.generator.get_all_recipes()
        self.assertIsInstance(recipes, list)
        for recipe in recipes:
            self.assertIsInstance(recipe, Recipe)
    
    def test_get_recipes_by_category(self):
        """Test filtering recipes by category."""
        breakfast_recipes = self.generator.get_recipes_by_category("breakfast")
        self.assertGreater(len(breakfast_recipes), 0)
        for recipe in breakfast_recipes:
            self.assertEqual(recipe.category, "breakfast")
        
        lunch_recipes = self.generator.get_recipes_by_category("lunch")
        self.assertGreater(len(lunch_recipes), 0)
        for recipe in lunch_recipes:
            self.assertEqual(recipe.category, "lunch")
    
    def test_get_recipes_by_invalid_category(self):
        """Test that invalid category returns empty list."""
        recipes = self.generator.get_recipes_by_category("invalid")
        self.assertEqual(len(recipes), 0)
    
    def test_get_random_recipe(self):
        """Test getting a random recipe."""
        recipe = self.generator.get_random_recipe()
        self.assertIsInstance(recipe, Recipe)
    
    def test_get_random_recipe_by_category(self):
        """Test getting a random recipe from a specific category."""
        recipe = self.generator.get_random_recipe("breakfast")
        self.assertIsInstance(recipe, Recipe)
        self.assertEqual(recipe.category, "breakfast")
    
    def test_get_random_recipe_invalid_category(self):
        """Test that invalid category raises an error."""
        with self.assertRaises(ValueError):
            self.generator.get_random_recipe("invalid")
    
    def test_search_recipes_by_name(self):
        """Test searching recipes by name."""
        results = self.generator.search_recipes("Pancakes")
        self.assertGreater(len(results), 0)
        found = any("Pancakes" in recipe.name for recipe in results)
        self.assertTrue(found)
    
    def test_search_recipes_by_ingredient(self):
        """Test searching recipes by ingredient."""
        results = self.generator.search_recipes("chicken")
        self.assertGreater(len(results), 0)
    
    def test_search_recipes_no_match(self):
        """Test searching with no matches."""
        results = self.generator.search_recipes("nonexistentingredient")
        self.assertEqual(len(results), 0)
    
    def test_search_recipes_case_insensitive(self):
        """Test that search is case-insensitive."""
        results_lower = self.generator.search_recipes("pancakes")
        results_upper = self.generator.search_recipes("PANCAKES")
        self.assertEqual(len(results_lower), len(results_upper))


if __name__ == '__main__':
    unittest.main()
