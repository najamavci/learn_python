from product import Product  

class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def total_price(self):
        return sum(product.get_price() for product in self.__products)