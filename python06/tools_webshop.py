from product import Product
from shopping_cart import ShoppingCart
from order import Order

# Example usage
p1 = Product(1, "Hammer", 15)
p2 = Product(2, "Screwdriver", 10)

cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)

order = Order(1001, cart)
order.print_order()

#outcome: Order total: 25