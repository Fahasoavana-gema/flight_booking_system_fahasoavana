from src import Flight, User


class Booking:
    def __init__(self, flight, user, staff):
        self.flight = flight
        self.user = user
        self.staff = staff

    def __str__(self):
        return f"{self.user}, a reservé {self.staff} sièges sur le vol {self.flight}"

    def cancel(self, flight: object):
        #print(self.flight, flight)
        if self.flight.flightid == flight.flightid:
            flight.currCapacity += self.staff
            return True
        else:
            return False
