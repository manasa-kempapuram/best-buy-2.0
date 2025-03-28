import product
import promotions
from store import Store

# Initialize products
product_list = [
    product.Product("MacBook Air M2", price=1450, quantity=100),
    product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    product.Product("Google Pixel 7", price=500, quantity=250),
    product.NonStockedProduct("Windows License", price=125),
    product.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half Price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Assign promotions to products
product_list[0].set_promotion(second_half_price)  # MacBook Air: Second item at half price
product_list[1].set_promotion(third_one_free)     # Bose Earbuds: Buy 2, Get 1 Free
product_list[3].set_promotion(thirty_percent)     # Windows License: 30% Discount

# Initialize store
best_buy = Store(product_list)

# Display products with promotions
for product in best_buy.get_all_active_products():
    print(product.show())

# Place an order with promotions
order_items = [
    (best_buy.products[0], 2),  # MacBook Air M2 (Second item half price)
    (best_buy.products[1], 3),  # Bose Earbuds (Buy 2, Get 1 Free)
    (best_buy.products[3], 1)   # Windows License (30% Off)
]

try:
    total_price = best_buy.order(order_items)
    print(f"Total Order Price: ${total_price}")
except ValueError as e:
    print(f"Order Failed: {e}")
