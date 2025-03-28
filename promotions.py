from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract base class for all promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Calculate the price after applying the promotion."""
        pass


class PercentDiscount(Promotion):
    """Applies a percentage discount to the product."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity


class SecondHalfPrice(Promotion):
    """Applies a discount where the second item is half price."""

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Applies a buy 2, get 1 free promotion."""

    def apply_promotion(self, product, quantity):
        full_price_items = quantity - (quantity // 3)
        return full_price_items * product.price
