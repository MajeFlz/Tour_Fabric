class Booking:
    def __init__(self, client, tour):
        self.client = client
        self.tour = tour

    def __str__(self):
        return f"Бронирование для {self.client.name} на тур в {self.tour.destination} по цене {self.tour.price}"