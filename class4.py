class Item:
    def __init__(self, name, price, quantity=0):
        # run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Initialise the object arguments
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("phone", 100, 5)
print(item1.name, item1.price, item1.quantity)
print(item1.calculate_total_price())

item2 = Item("laptop", 600, 3)
print(item2.name, item2.price, item2.quantity)
print(item2.calculate_total_price())
