# Create an application to store and retrieve recipes.
# Each recipe can include a name, list of ingredients and quantities. [cooking instructions is too much text]
# 
# To add:
# Upscale recipes: standard is 4 portions, but you can also make 2 or 6 and it adjusts accordingly
# Type in ingredients  you have and with a set comparison it checks which recipes e.g. use carrots AND potatoes
# checking if recipe already exists with .setdefault()
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
    control = str(input("(N)ew entry?\t(D)elete entry\t"))
    if control.upper() == "N":
        new_entry()
    elif control.upper() == "D":
        delete = str(input("Which entry do you want to delete? (Z)urück\t"))
        if delete.upper() != "Z":
            delete_check = str(input(f"Are you sure you want to delete {delete}? (Y)es or (N)o\t"))
            if delete_check.upper() == "Y":
                cookbook.pop(delete)
                open_cookbook(cookbook)
            if delete_check.upper() == "N":
                open_cookbook(cookbook)
        if delete.upper() == "Z":
            open_cookbook(cookbook)


def new_entry():
    new_dish = str(input("Add new dish:\t"))
    cookbook[new_dish] = {}
    x = 1
    while True:
        print(new_dish)
        new_ingredient = str(input(f"Please enter ingredient {x}:\t"))
        new_quantitiy = int(input(f"Please enter Quantity for {new_ingredient}:\t"))
        cookbook[new_dish][new_ingredient] = [new_quantitiy]
        control = str(input("(N)ext ingredient\n(S)ave and Exit\n(E)xit without saving\t"))
        if control.upper() == "N":
            x += 1
            continue
        if control.upper() == "S":
            open_cookbook(cookbook)
        if control.upper() == "E":
            cookbook.pop(new_dish)
            open_cookbook(cookbook)

open_cookbook(cookbook)
