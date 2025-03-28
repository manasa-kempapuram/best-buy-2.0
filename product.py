class Product:
    """Represents a product with name, price, and quantity."""

    def __init__(self, name, price, quantity):
        if not name or price < 0:
            raise ValueError("Invalid product details.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_active = quantity > 0

    def purchase(self, amount):
        """Handles product purchase and modifies quantity."""
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount
        if self.quantity == 0:
            self.is_active = False
        return self.price * amount

    def show(self):
        """Displays product details."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


# 🔹 **New Class: NonStockedProduct**
class NonStockedProduct(Product):
    """Represents a product with no stock tracking (e.g., software licenses)."""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)  # Quantity is always 0

    def purchase(self, amount):
        """NonStockedProduct can always be purchased (quantity isn't tracked)."""
        return self.price * amount

    def show(self):
        """Displays product details for non-stocked items."""
        return f"{self.name} (Non-Stocked), Price: ${self.price}"


# 🔹 **New Class: LimitedProduct**
class LimitedProduct(Product):
    """Represents a product with a purchase limit per order (e.g., shipping fees)."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # Max quantity per purchase

    def purchase(self, amount):
        """Ensures the product cannot be bought above the max limit in one order."""
        if amount > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} per order.")
        return super().purchase(amount)

    def show(self):
        """Displays product details for limited-stock items."""
        return f"{self.name} (Limited - Max {self.maximum}/order), Price: ${self.price}, Quantity: {self.quantity}"
