from abc import ABC, abstractmethod

class Promotion(ABC):
    """Abstract class for all promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    """Second item at half price."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Buy 2, get 1 free."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        return (quantity - free_items) * product.price


class PercentDiscount(Promotion):
    """Apply a percentage discount."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (product.price * self.percent) / 100
        return (product.price - discount) * quantity
