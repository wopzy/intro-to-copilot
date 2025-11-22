"""Unit tests for Meal Planner module."""

import unittest
from datetime import datetime, timedelta
from recipe_generator import Recipe, RecipeGenerator
from meal_planner import MealPlan, MealPlanner


class TestMealPlan(unittest.TestCase):
    """Test cases for the MealPlan class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.date = datetime(2024, 1, 1)
        self.meal_plan = MealPlan(self.date)
        self.recipe = Recipe(
            name="Test Recipe",
            ingredients=["ingredient1"],
            instructions=["step1"],
            prep_time=10,
            cook_time=20,
            servings=4,
            category="breakfast"
        )
    
    def test_meal_plan_creation(self):
        """Test that a meal plan can be created."""
        self.assertEqual(self.meal_plan.date, self.date)
        self.assertIsNone(self.meal_plan.breakfast)
        self.assertIsNone(self.meal_plan.lunch)
        self.assertIsNone(self.meal_plan.dinner)
        self.assertIsNone(self.meal_plan.snack)
    
    def test_add_meal(self):
        """Test adding meals to the plan."""
        self.meal_plan.add_meal("breakfast", self.recipe)
        self.assertEqual(self.meal_plan.breakfast, self.recipe)
    
    def test_add_meal_case_insensitive(self):
        """Test that meal type is case-insensitive."""
        self.meal_plan.add_meal("BREAKFAST", self.recipe)
        self.assertEqual(self.meal_plan.breakfast, self.recipe)
    
    def test_add_meal_invalid_type(self):
        """Test that invalid meal type raises an error."""
        with self.assertRaises(ValueError):
            self.meal_plan.add_meal("invalid", self.recipe)
    
    def test_get_meal(self):
        """Test retrieving meals from the plan."""
        self.meal_plan.add_meal("breakfast", self.recipe)
        retrieved = self.meal_plan.get_meal("breakfast")
        self.assertEqual(retrieved, self.recipe)
    
    def test_get_meal_not_set(self):
        """Test retrieving a meal that hasn't been set."""
        retrieved = self.meal_plan.get_meal("breakfast")
        self.assertIsNone(retrieved)
    
    def test_str_representation(self):
        """Test the string representation of a meal plan."""
        self.meal_plan.add_meal("breakfast", self.recipe)
        plan_str = str(self.meal_plan)
        self.assertIn("Monday", plan_str)
        self.assertIn("Test Recipe", plan_str)


class TestMealPlanner(unittest.TestCase):
    """Test cases for the MealPlanner class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.generator = RecipeGenerator()
        self.planner = MealPlanner(self.generator)
    
    def test_meal_planner_creation(self):
        """Test that a meal planner can be created."""
        self.assertIsInstance(self.planner.recipe_generator, RecipeGenerator)
        self.assertEqual(len(self.planner.meal_plans), 0)
    
    def test_create_weekly_plan(self):
        """Test creating a weekly meal plan."""
        start_date = datetime(2024, 1, 1)
        plans = self.planner.create_weekly_plan(start_date)
        
        self.assertEqual(len(plans), 7)
        
        # Verify each day has a plan
        for day in range(7):
            date = start_date + timedelta(days=day)
            date_key = date.replace(hour=0, minute=0, second=0, microsecond=0)
            self.assertIn(date_key, plans)
    
    def test_create_weekly_plan_with_all_meals(self):
        """Test creating a weekly plan with all meal types."""
        start_date = datetime(2024, 1, 1)
        plans = self.planner.create_weekly_plan(
            start_date,
            include_breakfast=True,
            include_lunch=True,
            include_dinner=True,
            include_snack=True
        )
        
        # Check first day has all meals
        first_plan = plans[start_date]
        self.assertIsNotNone(first_plan.breakfast)
        self.assertIsNotNone(first_plan.lunch)
        self.assertIsNotNone(first_plan.dinner)
        self.assertIsNotNone(first_plan.snack)
    
    def test_create_weekly_plan_selective_meals(self):
        """Test creating a plan with only selected meal types."""
        start_date = datetime(2024, 1, 1)
        plans = self.planner.create_weekly_plan(
            start_date,
            include_breakfast=True,
            include_lunch=False,
            include_dinner=True,
            include_snack=False
        )
        
        first_plan = plans[start_date]
        self.assertIsNotNone(first_plan.breakfast)
        self.assertIsNone(first_plan.lunch)
        self.assertIsNotNone(first_plan.dinner)
        self.assertIsNone(first_plan.snack)
    
    def test_get_plan_for_date(self):
        """Test retrieving a meal plan for a specific date."""
        start_date = datetime(2024, 1, 1)
        self.planner.create_weekly_plan(start_date)
        
        plan = self.planner.get_plan_for_date(start_date)
        self.assertIsInstance(plan, MealPlan)
        self.assertEqual(plan.date, start_date)
    
    def test_get_plan_for_date_not_found(self):
        """Test retrieving a plan for a date that doesn't exist."""
        plan = self.planner.get_plan_for_date(datetime(2024, 1, 1))
        self.assertIsNone(plan)
    
    def test_get_shopping_list(self):
        """Test generating a shopping list."""
        start_date = datetime(2024, 1, 1)
        self.planner.create_weekly_plan(start_date)
        
        shopping_list = self.planner.get_shopping_list()
        self.assertIsInstance(shopping_list, dict)
        self.assertGreater(len(shopping_list), 0)
        
        # Verify structure
        for recipe_name, ingredients in shopping_list.items():
            self.assertIsInstance(recipe_name, str)
            self.assertIsInstance(ingredients, list)
    
    def test_get_shopping_list_empty_plan(self):
        """Test shopping list with no meal plan."""
        shopping_list = self.planner.get_shopping_list()
        self.assertEqual(len(shopping_list), 0)


if __name__ == '__main__':
    unittest.main()
