class Order:
    def __init__(self, order_number, product, quantity, price):
        self._order_number = order_number
        self.product = product
        self.quantity = quantity
        self.price = price

    @property
    def order_number(self):
        return self._order_number

    def display_order_info(self):
        print(f"Order Number: {self.order_number}")
        print(f"Product: {self.product}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price}")


order = Order(order_number=1001, product="Laptop", quantity=2, price=1200.0)

print("Order Number:", order.order_number)

order.order_number = 1002

order.display_order_info()