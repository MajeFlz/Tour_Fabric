from factory import TourFactory
from observer import TourAgency
from models.client import Client

if __name__ == "__main__":
    factory = TourFactory()
    agency = TourAgency()

    tour1 = factory.create_tour("Париж", 1000)
    tour2 = factory.create_tour("Турция", 800)

    agency.add_tour(tour1)
    agency.add_tour(tour2)

    client1 = Client("Иван")
    client2 = Client("Анна")
    client3 = Client("Григорий")

    agency.add_client(client1)
    agency.add_client(client2)
    agency.add_client(client3)

    booking1 = client1.book_tour(tour1)
    booking2 = client2.book_tour(tour2)
    booking3 = client3.book_tour(tour1)

    agency.change_tour_price(tour1, 900)
    agency.change_tour_price(tour2, 650)

    print(booking1)
    print(booking2)
    print(booking3)