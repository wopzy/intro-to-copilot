"""Meal Planner Module

This module provides functionality to plan meals for a week using recipes.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
from recipe_generator import Recipe, RecipeGenerator


class MealPlan:
    """Represents a meal plan for a specific day."""
    
    def __init__(self, date: datetime):
        """
        Initialize a meal plan for a specific date.
        
        Args:
            date: The date for this meal plan
        """
        self.date = date
        self.breakfast: Optional[Recipe] = None
        self.lunch: Optional[Recipe] = None
        self.dinner: Optional[Recipe] = None
        self.snack: Optional[Recipe] = None
    
    def add_meal(self, meal_type: str, recipe: Recipe):
        """
        Add a recipe to a specific meal slot.
        
        Args:
            meal_type: Type of meal (breakfast, lunch, dinner, snack)
            recipe: Recipe to add
        """
        meal_type_lower = meal_type.lower()
        if meal_type_lower == "breakfast":
            self.breakfast = recipe
        elif meal_type_lower == "lunch":
            self.lunch = recipe
        elif meal_type_lower == "dinner":
            self.dinner = recipe
        elif meal_type_lower == "snack":
            self.snack = recipe
        else:
            raise ValueError(f"Invalid meal type: {meal_type}")
    
    def get_meal(self, meal_type: str) -> Optional[Recipe]:
        """
        Get the recipe for a specific meal type.
        
        Args:
            meal_type: Type of meal to retrieve
            
        Returns:
            Recipe for the meal type, or None if not set
        """
        meal_type_lower = meal_type.lower()
        if meal_type_lower == "breakfast":
            return self.breakfast
        elif meal_type_lower == "lunch":
            return self.lunch
        elif meal_type_lower == "dinner":
            return self.dinner
        elif meal_type_lower == "snack":
            return self.snack
        return None
    
    def __str__(self) -> str:
        """Return a formatted string representation of the meal plan."""
        date_str = self.date.strftime("%A, %B %d, %Y")
        result = [f"\n{date_str}", "=" * len(date_str)]
        
        if self.breakfast:
            result.append(f"\nBreakfast: {self.breakfast.name}")
        if self.lunch:
            result.append(f"Lunch: {self.lunch.name}")
        if self.dinner:
            result.append(f"Dinner: {self.dinner.name}")
        if self.snack:
            result.append(f"Snack: {self.snack.name}")
        
        return "\n".join(result)


class MealPlanner:
    """Plans meals for a week using available recipes."""
    
    def __init__(self, recipe_generator: RecipeGenerator):
        """
        Initialize the meal planner.
        
        Args:
            recipe_generator: RecipeGenerator instance to use for recipes
        """
        self.recipe_generator = recipe_generator
        self.meal_plans: Dict[datetime, MealPlan] = {}
    
    def create_weekly_plan(self, start_date: datetime = None, 
                          include_breakfast: bool = True,
                          include_lunch: bool = True,
                          include_dinner: bool = True,
                          include_snack: bool = False) -> Dict[datetime, MealPlan]:
        """
        Create a meal plan for a week.
        
        Args:
            start_date: Starting date for the plan (defaults to today)
            include_breakfast: Whether to plan breakfasts
            include_lunch: Whether to plan lunches
            include_dinner: Whether to plan dinners
            include_snack: Whether to plan snacks
            
        Returns:
            Dictionary mapping dates to MealPlan objects
        """
        if start_date is None:
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        self.meal_plans = {}
        
        for day in range(7):
            current_date = start_date + timedelta(days=day)
            meal_plan = MealPlan(current_date)
            
            if include_breakfast:
                breakfast = self.recipe_generator.get_random_recipe("breakfast")
                meal_plan.add_meal("breakfast", breakfast)
            
            if include_lunch:
                lunch = self.recipe_generator.get_random_recipe("lunch")
                meal_plan.add_meal("lunch", lunch)
            
            if include_dinner:
                dinner = self.recipe_generator.get_random_recipe("dinner")
                meal_plan.add_meal("dinner", dinner)
            
            if include_snack:
                snack = self.recipe_generator.get_random_recipe("snack")
                meal_plan.add_meal("snack", snack)
            
            self.meal_plans[current_date] = meal_plan
        
        return self.meal_plans
    
    def get_plan_for_date(self, date: datetime) -> Optional[MealPlan]:
        """
        Get the meal plan for a specific date.
        
        Args:
            date: Date to retrieve plan for
            
        Returns:
            MealPlan for the date, or None if not planned
        """
        date_key = date.replace(hour=0, minute=0, second=0, microsecond=0)
        return self.meal_plans.get(date_key)
    
    def get_shopping_list(self) -> Dict[str, List[str]]:
        """
        Generate a shopping list for all planned meals.
        
        Returns:
            Dictionary mapping recipe names to their ingredients
        """
        shopping_list = {}
        
        for meal_plan in self.meal_plans.values():
            for meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                recipe = meal_plan.get_meal(meal_type)
                if recipe:
                    shopping_list[recipe.name] = recipe.ingredients
        
        return shopping_list
    
    def print_weekly_plan(self):
        """Print the entire weekly meal plan."""
        if not self.meal_plans:
            print("No meal plan created yet. Use create_weekly_plan() first.")
            return
        
        print("\n" + "=" * 60)
        print("WEEKLY MEAL PLAN")
        print("=" * 60)
        
        for date in sorted(self.meal_plans.keys()):
            print(self.meal_plans[date])
        
        print("\n" + "=" * 60)
    
    def print_shopping_list(self):
        """Print the shopping list for all planned meals."""
        shopping_list = self.get_shopping_list()
        
        if not shopping_list:
            print("No shopping list available. Create a meal plan first.")
            return
        
        print("\n" + "=" * 60)
        print("SHOPPING LIST")
        print("=" * 60)
        
        for recipe_name, ingredients in shopping_list.items():
            print(f"\n{recipe_name}:")
            for ingredient in ingredients:
                print(f"  - {ingredient}")
        
        print("\n" + "=" * 60)
