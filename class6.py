class Item:
    # The pay after 20% dicount
    pay_rate = 0.8 
    all = []

    def __init__(self, name, price, quantity=0):
        # run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Initialise the object arguments
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_dicount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("Mouse", 58, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.name)
