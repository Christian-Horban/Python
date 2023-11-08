# Initialize empty lists
recipes_list = []
ingredients_list = []

# Define the take_recipe function
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    n_ingredients = int(input("Enter the number of ingredients: "))
    for i in range(n_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

# Ask the user how many recipes they want to enter
n = int(input("How many recipes would you like to enter?"))

# Loop to take recipes
for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    # Add unique ingredients to ingredients_list
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

# Determine the difficulty of each recipe
for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    if cooking_time < 10 and num_ingredients < 4:
        recipe['difficulty'] = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        recipe['difficulty'] = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        recipe['difficulty'] = 'Intermediate'
    else:
        recipe['difficulty'] = 'Hard'

# Display all unique ingredients in alphabetical order
print("All Ingredients Used:")
for ingredient in sorted(ingredients_list):
    print(f"- {ingredient}")

# Print the recipes and their difficulty
for recipe in recipes_list:
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty level: {recipe['difficulty']}")
    print()