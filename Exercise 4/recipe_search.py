import pickle


# Function to display a recipe
def display_recipe(recipe):
    print(f"Recipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}\n")


# Function to search for an ingredient
def search_ingredient(data):
    print("Available Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(f"{index}. {ingredient}")

    try:
        choice = int(
            input("Enter the number of the ingredient you want to search for: ")
        )
        ingredient_searched = data["all_ingredients"][choice]
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid number.")
    else:
        print(f"\nRecipes containing {ingredient_searched}:")
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)


# Main code
filename = input("Enter the filename of your recipe data: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the filename and try again.")
else:
    search_ingredient(data)
