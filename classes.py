
class Place:
    def __init__(self, name):
        self.name = name


class Event:
    def __init__(self, type, name, all_tickets, sold_tickets, price, date, time):
        self.type = type
        self.name = name
        self.all_tickets = all_tickets
        self.sold_tickets = sold_tickets
        self.price = price
        self.date = date
        self.time = time
