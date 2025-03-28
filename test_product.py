import pytest
from product import Product, NonStockedProduct, LimitedProduct

def test_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active is True

def test_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price

def test_zero_quantity():
    product = Product("Google Pixel 7", price=500, quantity=1)
    product.purchase(1)  # Buying all available stock
    assert product.quantity == 0
    assert product.is_active is False

def test_modify_quantity():
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    cost = product.purchase(3)
    assert product.quantity == 7  # 10 - 3 = 7
    assert cost == 750  # 3 * 250 = 750

def test_larger_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.purchase(10)  # Trying to buy more than available


def test_non_stocked_product():
    product = NonStockedProduct("Windows License", price=125)

    # Test if quantity is always zero
    assert product.quantity == 0  # Always zero

    # Test if purchasing raises an exception
    with pytest.raises(ValueError, match="Cannot purchase non-stocked products."):
        product.purchase(10)  # Attempt to purchase, should raise exception


def test_limited_product():
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.purchase(2)  # Cannot buy more than 1 per order
    cost = product.purchase(1)
    assert cost == 10  # Successful purchase
