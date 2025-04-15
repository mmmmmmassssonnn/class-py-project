# Purpose: A menu for a coffee shop
# Date:
# Programmers:

import json

class Order:
    def __init__(self, price, order):
        self.price = price
        self.order = order

    def orderFormat(self):
        # do a return with the order formatted here
        pass

# Define Constants
subtotal = 0 # Total Before Tax
total = subtotal * 1.07 # Total After
full_order = []

keep_going = True # The loop should keep going

# Potential items: Espresso, Latte, Cappuccino, Muffins, Croissants
# Prices: 3, 4, 3.5, 2, 5
# tax rate: 0.07
# Discounts: Codes: 5OFF, SENIOR, SECRET
# Payment method: Cash, Card

with open('menu.json', 'r') as file:
    data = json.load(file)

def get_menu_item(menuitem):
    option = next(
        (item for item in data if item["shorthand"] == menuitem), None
    )
    if option:
        return option["price"]
    return None

print(get_menu_item("Es"))

#print(data["Espresso"])

while keep_going == True:
    pass
