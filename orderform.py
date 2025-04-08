class Order:
    def __init__(self, price, order):
        self.price = price
        self.order = order

    def orderFormat(self):
        # do a return with the order formatted here

# Define Constants
subtotal = 0 # Total Before Tax
total = subtotal * 1.07 # Total After Tax

keepgoing = true # The loop should keep going

# Potential items: Espresso, Latte, Cappuccino, Muffins, Croissants
# Prices: 3, 4, 3.5, 2, 5
# tax rate: 0.07
# Discounts: Codes: 5OFF, SENIOR, SECRET
# Payment method: Cash, Card
