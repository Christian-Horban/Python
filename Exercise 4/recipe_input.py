import pickle


# Define the calc_difficulty function
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"


# take_recipe function
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    n_ingredients = int(input("Enter the number of ingredients: "))
    for i in range(n_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)

    difficulty = calc_difficulty(cooking_time, n_ingredients)
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


# Main code
filename = input("Enter the filename for storing recipes: ")

# Try-except-else-finally block for file handling
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except Exception:
    data = {"recipes_list": [], "all_ingredients": []}
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

# Ask how many recipes to enter
n = int(input("How many recipes would you like to enter?"))

# Loop to take recipes
for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    # Add unique ingredients to all_ingredients
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Update the data dictionary
data["recipes_list"] = recipes_list
data["all_ingredients"] = all_ingredients

# Write data to a binary file
with open(filename, "wb") as file:
    pickle.dump(data, file)
