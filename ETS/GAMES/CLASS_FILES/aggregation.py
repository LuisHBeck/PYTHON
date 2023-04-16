class Cart:
    def __init__(self) -> None:
        self._products = []

    def add_products(self, *products):
        for product in products:
            self._products.append(product)

    def total(self):
        return sum([p.price for p in self._products])
    
    def list_products(self):
        for product in self._products:
            print(f'Name = {product.name} / Price = ${product.price}')

class Product():
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        

if __name__ == "__main__":
    cart = Cart()
    pen = Product('Pen', 15)
    shirt = Product('Shirt', 25)
    cart.add_products(pen, shirt)
    cart.list_products()
    print(cart.total())
