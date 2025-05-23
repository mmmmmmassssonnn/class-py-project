# Purpose: A menu for a coffee shop
# Date: April 21, 2025
# Programmers: Mason, Naseem

# Algorithm
# I. Input
#   A. Display menu
#   B. Get user input for items
#   C. Get user input for discounts if any
# II. Process
#   A. With each item, update running subtotal
#   B. With the discounts, use a function to update the subtotal
# III. Output
#   A. Display the items ordered
#   B. Display the total with tax
#   C. Display a greeting message
# IV. End.

import json

# Define Constants
subtotal = 0 # Total Before Tax
full_order = []

keep_going = True # The loop should keep going

def discount_handler(code, sub): # Handle discounts
    if code == "5OFF":
        subtotal = sub *.95
        return subtotal
    if code == "SENIOR":
        subtotal = sub *.95
        return subtotal
    if code == "SECRET":
        subtotal = sub *.90
        return subtotal
    else: return "404"

with open('menu.json', 'r') as file: # Open the menu json file
    data = json.load(file)

# ☕ Fun & Emoji-Filled Menu Preview 
print("\n☕ Welcome to COFFEE CODE 💻")
print("Where every sip fuels your next big idea!\n")
print("Here's what we're brewing today:\n")

emoji_map = {
    "Espresso": "☕",
    "Latte": "🥛",
    "Cappuccino": "🍶",
    "Muffins": "🧁",
    "Croissants": "🥐"
}

for item in data:
    emoji = emoji_map.get(item["name"], "")
    print(f"  🔹 [{item['shorthand']}] {item['name']} {emoji} — ${item['price']:.2f}")

print("\n(Use the item shorthand to order, like 'Es' for Espresso!)\n")

def get_name(menuitem): # Get the name of a menu item from shorthand
    option = next(
        (item for item in data if item["shorthand"] == menuitem), None
    )
    if option:
        return option["name"]
    return None

def get_price(menuitem): # Get price of a menu item from shorthand
    option = next(
        (item for item in data if item["shorthand"] == menuitem), None
    )
    if option:
        return option["price"]
    return None

while keep_going == True: # Start the loop
    product_choice = input("Please enter the item you'd like to buy ")
    try: # Try/Except for getting the prices and such
        subtotal += get_price(product_choice)
        full_order.append(get_name(product_choice))
    except:
        print("Please enter a valid item.")
        break
    another_order = input("Do you have another order [Y/N]: ") # Another order?
    if another_order.lower() == "n": keep_going = False

discount_prompt = input("Do you have a discount code [Y/N]: ") # Do they have a code
if discount_prompt.lower() == "y":
    disc_code = input("Please enter your discount code ") # Enter code
    try_discount = discount_handler(disc_code.upper(), subtotal)
    if try_discount != '404': # See if valid
        print('Successfully applied discount.')
        subtotal = try_discount # Update subtotal
    else: print('Invalid discount code.')
print("You have ordered the following items:") # Print the order
for item in full_order:
    print(item, end=" | ")
print()
total = subtotal * 1.07 # Total After
print(f'For a total cost of ${total:.2f}')
print("Thank you for your order and come again!")

# End.
