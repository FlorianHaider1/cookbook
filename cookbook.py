# Create an application to store and retrieve recipes.
# Each recipe can include a name, list of ingredients and quantities. [cooking instructions is too much text]
# 
# input console should work like that:
# Insert recipe name (checks if it is there)
# Insert Ingredient#1 
# Insert Quantity for Ingredient#1
# Then ask: another ingredient or done?

# To add:
# Upscale recipes: standard is 4 portions, but you can also make 2 or 6 and it adjusts accordingly
# Type in ingredients  you have and with a set comparison it checks which recipes e.g. use carrots AND potatoes
# 
# Practice Skills:
# Use a dictionary to map recipe names to their details.
# Ingredients can be stored in tuples (ingredient, quantity) within a list.
# Practice adding new recipes, updating existing ones, and retrieving a recipe by name.
# Use slicing and string methods for displaying and formatting recipes.
from prettytable import PrettyTable
cookbook = {}    
cookbook["vegetable soup"] = {"carrots":5, "potatoes":3, "leek":1}
cookbook["chicken curry"] = {"chicken":1, "carrots":2, "curry":1}

def open_cookbook(book):
    table = PrettyTable()
    table.field_names = ["Dish", "Ingredient", "Quantity"]
    for dish, ingredients in book.items():
        table.add_row([dish,"",""])
        for type, quantity in ingredients.items():
            print(type)
            print(quantity)
            table.add_row(["",type, quantity])
        table.add_row(["","",""])
    print(table)
    navigation()

def navigation():
    control = str(input("(N)ew Entry?"))
    if control.upper() == "N":
        new_entry()

def new_entry():
    new_dish = "Spaghetti Bolognese"
    cookbook[new_dish] = {}
    x = 1
    while True:
        print(new_dish)
        new_ingredient = str(input(f"Please enter ingredient {x}: "))
        new_quantitiy = int(input(f"Please enter Quantity for {new_ingredient}: "))
        cookbook[new_dish][new_ingredient] = [new_quantitiy]
        control = str(input("(N)ext ingredient\n(S)ave and Exit\n(E)xit without saving"))
        if control.upper() == "N":
            x += 1
            continue
        if control.upper() == "S":
            open_cookbook(cookbook)
        if control.upper() == "E":
            cookbook.pop(new_dish)
            open_cookbook(cookbook)

open_cookbook(cookbook)
new_entry()
