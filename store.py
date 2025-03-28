class Store:
    """Represents a store managing a list of products."""

    def __init__(self, products):
        """Initialize store with a list of products."""
        self.products = products  # List of Product, NonStockedProduct, and LimitedProduct objects

    def add_product(self, product):
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum(product.quantity for product in self.products if hasattr(product, 'quantity'))

    def get_all_active_products(self):
        """Return a list of all active (in-stock) products."""
        return [product for product in self.products if product.is_active]

    def order(self, shopping_list):
        """
        Processes an order from a list of (product, quantity) tuples.
        Returns the total cost of the order.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.purchase(quantity)  # Calls the appropriate purchase method

        return total_cost


