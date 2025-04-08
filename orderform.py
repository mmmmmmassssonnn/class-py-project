class Order:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def orderFormat(self):
        # do a return with the order formatted here

# Define Constants
subtotal = 0 # Total Before Tax
total = subtotal * 1.07 # Total After Tax
