class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products: {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        print(f"Original Price: {price}, discount: {discount},Final Price: {price - (price * discount / 100)}")

P1 = Product("Laptop", 1200)
P2 = Product("Smartphone", 800)
P1.get_info()
P2.get_info()
Product.get_count()
print(P1.get_discount(P1.price, 15))
print(P2.get_discount(P2.price, 10))