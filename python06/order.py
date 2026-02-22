from shopping_cart import ShoppingCart

class Order:
    def __init__(self, id, cart):
        self.__id = id
        self.__cart = cart

    def print_order(self):
        print("Order total:", self.__cart.total_price())