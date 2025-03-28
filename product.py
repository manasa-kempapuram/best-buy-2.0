class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_active = quantity > 0

    def purchase(self, amount: int):
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount
        if self.quantity == 0:
            self.is_active = False
        return self.price * amount
