import pytest
from product import Product


def test_normal_product():
    product = Product("Laptop", price=1450, quantity=100)
    assert product.name == "Laptop"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active is True


def test_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", price = 1450, quantity = 100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price = -10, quantity = 100)

def test_zero_quantity():
    product = Product("Smartphone", price = 500, quantity = 1)
    product.purchase(1)  # Buying all available stock
    assert product.quantity == 0
    assert product.is_active is False


def test_modify_quantity():
    product = Product("Headphones", price = 50, quantity = 10)
    cost = product.purchase(3)
    assert product.quantity == 7  # 10 - 3 = 7
    assert cost == 150  # 3 * 50 = 150


def test_larger_quantity():
    product =Product("Game station", price = 1500, quantity = 5 )
    with pytest.raises(ValueError):
        product.purchase(10)  # Trying to buy more than available
