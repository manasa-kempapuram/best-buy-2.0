class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity):
        if not name or price < 0:
            raise ValueError("Invalid product name or price.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_active = True
        self.promotion = None  # New attribute for promotions

    def set_promotion(self, promotion):
        """Assign a promotion to the product."""
        self.promotion = promotion

    def show(self):
        """Display product details including promotion (if any)."""
        promotion_text = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name} - ${self.price} ({self.quantity} in stock){promotion_text}"

    def purchase(self, quantity):
        """Process a purchase, applying promotions if available."""
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_cost = self.promotion.apply_promotion(self, quantity)
        else:
            total_cost = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.is_active = False

        return total_cost


class NonStockedProduct(Product):
    """Product that is not stocked, always has quantity 0."""

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        """Override show to indicate no stock."""
        return f"{self.name} - ${self.price} (Non-stocked)"

    def purchase(self, quantity):
        """No purchase possible for non-stocked products."""
        raise ValueError("Cannot purchase non-stocked products.")


class LimitedProduct(Product):
    """Product that has a limited purchase quantity."""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def purchase(self, quantity):
        """Override purchase to enforce the maximum limit."""
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of this product.")
        return super().purchase(quantity)
