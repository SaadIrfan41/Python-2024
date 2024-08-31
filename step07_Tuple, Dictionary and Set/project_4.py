# Restaurant Menu Manager

# ? Objective
# Imagine you're a developer, and a local restaurant wants your help to manage their menu. They need a program to easily update their menu and count how many types of dishes (like appetizers, mains, desserts) they have.

# ? Instructions
# Create the Menu:

# Make a dictionary called menu where the keys are dish names, and the values are tuples containing the dish type and price.
# Start with these dishes: 'Burger', 'Soup', 'Ice Cream', 'Salad'.
# Example format: {'Burger': ('Main', 10.5), 'Soup': ('Appetizer', 5.0)}
# Add Dishes:

# Add two more dishes to the menu: 'Steak' and 'Soda'.
# Remove a Dish:

# Remove one dish from the menu.
# Display the Menu:

# Write a function called display_menu that shows all the dishes with their type and price.
# Count Dish Types:

# Write a function called count_dish_types that counts how many of each type of dish there are (e.g., how many mains, appetizers, etc.).
# Update the Price:

# Write a function called update_price that changes the price of a dish. This function should take the menu, a dish name, and the new price as inputs.
# Use the Functions:

# Use all the functions you've written to manage the menu and show the updated details.

# Step 1: Initial menu

# Step 2: Add dishes

# Step 3: Remove dish

# Step 4: Display menu function

# Step 5: Count dish types function

# Step 6: Update price function

# Step 7: Use all functions to manage menu

# ? Example Output
# Initial Menu:

# Soup - Appetizer: $5.00
# Ice Cream - Dessert: $3.50
# Soda - Drink: $2.00
# Burger - Main: $10.50
# Steak - Main: $20.00
# Dish Types Count:

# {'Appetizer': 1, 'Dessert': 1, 'Drink': 1, 'Main': 2}
# Updated Menu After Price Change:

# Soup - Appetizer: $5.50
# Ice Cream - Dessert: $3.50
# Soda - Drink: $2.00
# Burger - Main: $10.50
# Steak - Main: $20.00

######################################################################
# ? CODE
menu = {
    "Burger": ("Main", 10.5),
    "Soup": ("Appetizer", 5.0),
    "Ice Cream": ("Dessert", 3.5),
    "Salad": ("Appetizer", 4.0),
}

# def display_menu(menu):
#     print("Menu:")
#     for dish, (dish_type, price) in menu.items():
#         print(f"{dish} - {dish_type}: ${price:.2f}")

# dish_types = {}
# for value in menu.values():
#     if value[0] in dish_types:
#         dish_types[value[0]] += 1
#     else:
#         dish_types[value[0]] = 1

# print(dish_types)


# def update_price(dish_name, price):
#     formated_price = float(f"{price:.2f}")
#     if dish_name in menu:
#         menu[dish_name] = (dish_name, formated_price)
#         print(menu)
#     else:
#         print(f"Dish Name {dish_name} does not exist in our menu")


# update_price("Salad", 50)
