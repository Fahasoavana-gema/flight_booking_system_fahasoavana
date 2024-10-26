class Flight:
    def __init__(self, flightid, fromloc, toloc, capacity, currCapacity):
        self.flightid = flightid
        self.fromloc = fromloc
        self.toloc = toloc
        self.capacity = capacity
        self.currCapacity = currCapacity

    def __str__(self):
        return f"{self.flightid} ({self.fromloc} - {self.toloc}) - {self.capacity} ({self.currCapacity} restants)"
    
    def book(self, staff):
        if staff <= self.currCapacity:
            self.currCapacity -= staff
            return True
        else:
            return False
    