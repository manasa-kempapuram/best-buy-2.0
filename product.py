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
