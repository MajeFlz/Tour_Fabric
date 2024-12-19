class TourAgency:
    def __init__(self):
        self.tours = []
        self.clients = []

    def add_tour(self, tour):
        self.tours.append(tour)

    def add_client(self, client):
        self.clients.append(client)

    def get_clients_for_tour(self, tour):
        return [client for client in self.clients if client.has_booking(tour)]

    def notify_clients(self, tour):
        clients_to_notify = self.get_clients_for_tour(tour)
        for client in clients_to_notify:
            client.update(tour)

    def change_tour_price(self, tour, new_price):
        if tour in self.tours:
            tour.set_price(new_price)
            self.notify_clients(tour)
        else:
            raise ValueError("Тур не найден в списке турагентства.")