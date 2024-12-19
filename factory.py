from models.tour import Tour

class TourFactory:
    @staticmethod
    def create_tour(destination, price):
        return Tour(destination, price)