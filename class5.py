class Item:
    # The pay after 20% dicount
    pay_rate = 0.8 

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

    def apply_dicount(self):
        self.price = self.price * self.pay_rate


item1 = Item("phone", 100, 5)
item1.apply_dicount()
print(item1.price)
print(item1.__dict__)

item2 = Item("laptop", 600, 3)
item2.apply_discount()
print(item2.price)
