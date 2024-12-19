class Tour:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    def set_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"Тур в {self.destination} по цене {self.price}"