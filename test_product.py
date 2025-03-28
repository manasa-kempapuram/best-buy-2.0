import pytest
from product import Product
from store import Store  # Assuming you have a Store class managing inventory

# 🔹 Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# 🔹 Initialize the store
best_buy = Store(product_list)

# 🔹 Test the new products
print(best_buy.products[3].show())  # Windows License (Non-Stocked), Price: $125
print(best_buy.products[4].show())  # Shipping (Limited - Max 1/order), Price: $10, Quantity: 250

# 🔹 Test purchasing
print(best_buy.products[3].purchase(5))  # Buying 5 Windows Licenses (No stock tracking)
print(best_buy.products[4].purchase(1))  # Buying 1 shipping fee (Valid)

# 🔹 Test exceeding limit
try:
    best_buy.products[4].purchase(2)  # Should raise an exception
except ValueError as e:
    print(e)  # Expected output: Cannot buy more than 1 per order.





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
