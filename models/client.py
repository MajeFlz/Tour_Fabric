from models.booking import Booking

class Client:
    def __init__(self, name):
        self.name = name
        self.bookings = []

    def update(self, tour):
        print(f"{self.name}, цена вашего тура в {tour.destination} изменилась на {tour.price}!")

    def book_tour(self, tour):
        booking = Booking(self, tour)
        self.bookings.append(booking)
        return booking

    def has_booking(self, tour):
        return any(booking.tour == tour for booking in self.bookings)