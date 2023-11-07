# Recipe Repository

## Step 1: Create Recipe Structure

## Recipe Structures

```python
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

# Creating the all_recipes Structure
all_recipes = [recipe_1]

# Create additional recipes following recipe_1 structure

all_recipes.extend([recipe_2, recipe_3, recipe_4, recipe_5])

# Printing Ingredients for Each Recipe
for i, recipe in enumerate(all_recipes, start=1):
    print(f"Ingredients for Recipe {i}: {recipe['ingredients']}")
