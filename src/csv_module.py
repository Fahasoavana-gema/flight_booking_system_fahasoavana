import csv
from src import Flight, User
def flight_csv_read(cls, file_path):
    flights = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            flight = cls(
                flightid=row['flightid'],
                fromloc=row['fromloc'],
                toloc=row['toloc'],
                capacity=int(row['capacity']),
                currCapacity=int(row['currcapacity'])
            )
            flights.append(flight)
    return flights

def booking_csv_read(cls, file_path):
    bookings = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            booking = cls(
                flight = Flight(row['flightid'], row['fromloc'], row['toloc'], int(row['capacity']), int(row['currcapacity'])),

                user = User(row['username'], int(row['userage'])),
                staff = int(row['staff'])
            )
            bookings.append(booking)
    return bookings

def booking_csv_save(file_path, bks):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['flightid', 'fromloc', 'toloc', 'capacity', 'currcapacity','username', 'userage','staff'])

        for bk in bks:
            writer.writerow([
                bk.flight.flightid,
                bk.flight.fromloc,
                bk.flight.toloc,
                bk.flight.capacity,
                bk.flight.currCapacity,
                bk.user.name,
                bk.user.age,
                bk.staff
            ])

def flight_csv_save(file_path, fls):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['flightid', 'fromloc', 'toloc', 'capacity', 'currcapacity'])
        for fl in fls:
            writer.writerow([
                fl.flightid,
                fl.fromloc,
                fl.toloc,
                fl.capacity,
                fl.currCapacity
            ])