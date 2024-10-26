from src import Flight, User, Booking
from src.csv_module import flight_csv_read, booking_csv_read, booking_csv_save, flight_csv_save

import csv

def launch_menu():
    print("\nMenu :")
    print("1. Afficher les vols")
    print("2. Vérifier la disponibilité des sièges")
    print("3. Réserver un vol")
    print("4. Annuler une réservation")
    print("5. Quitter")
    choice = input("Choisissez une option : ")
    return choice

def show_flights():
    flights = flight_csv_read(Flight, 'data/flightsdata.csv')
    for flight in flights:
        print(flight)
def get_flight(input_fid, fls):
    flight = next((f for f in fls if f.flightid == input_fid), None)
    return flight

def get_flight_index(input_fid, fls):
    findex = next((i for i, f in enumerate(fls) if f.flightid == input_fid), None)
    return findex

def get_booking(input_fl, input_user, bks):
    #for b in bks:
    #    print(b.user.name, input_user)
    bk = next((b for b in bks if b.flight.flightid.strip() == input_fl.strip() and b.user.name.strip() == input_user.strip()), None)
    #print(bk)

    return bk

def get_booking_index(bk, bks):
    bkindex = next((i for i, b in enumerate(bks) if b == bk ), None)
    return bkindex

def check_seats():
    input_fid = input("Entrez la référence du vol que vous souhaitez vérifier : ")
    flights = flight_csv_read(Flight, "data/flightsdata.csv")
    flight = get_flight(input_fid, flights)

    if flight is None:
        print("Le vol n'existe pas.")
        return

    print(f"Le vol {flight.flightid} a {flight.currCapacity} sièges disponibles.")


def book_flight():
    flights = flight_csv_read(Flight, "data/flightsdata.csv")
    bookings = booking_csv_read(Booking, "data/bookingsdata.csv")

    input_fid = input("Entrez la référence du vol que vous souhaitez réserver : ")
    flight = get_flight(input_fid, flights)
    flight_index = get_flight_index(input_fid, flights)

    if flight is None:
        print("Le vol n'existe pas.")
        return

    user = User(input("Entrez votre nom : "), int(input("Entrez votre âge : ")))

    staff = int(input("Combien de sièges voulez-vous réserver ? "))
    # print(findex)

    if flight.book(staff):
        flights[flight_index] = flight
        booking = Booking(flight, user, staff)
        bookings.append(booking)
        print(booking)

        flight_csv_save('data/flightsdata.csv', flights)
        booking_csv_save('data/bookingsdata.csv', bookings)
    else:
        print("Réservation échouée : pas assez de sièges disponibles.")

def cancel_booking():
    #Chargement
    flights = flight_csv_read(Flight, "data/flightsdata.csv")
    bookings = booking_csv_read(Booking, "data/bookingsdata.csv")

    input_fl = input("Entrez la référence du vol que vous souhaitez annuler : ")

    flight = get_flight(input_fl, flights)
    if flight is None:
        print("Le vol n'existe pas.")
        return
    flight_index = get_flight_index(flight.flightid, flights)

    input_user = input("Entrez votre nom d'utilisateur : ")
    #print([bk for bk in bookings])

    booking = get_booking(input_fl, input_user, bookings)
    #print(booking)
    if booking is None:
        print("Cette réservation n'existe pas !")
        return

    booking_index = get_booking_index(booking, bookings)

    # Actions
    if booking.cancel(flight):
        del bookings[booking_index]
        flights[flight_index] = flight

        print(f"Annulation réussie pour {input_user}. Sièges restants : {flight.currCapacity}")

    # Sauvegardes
    flight_csv_save('data/flightsdata.csv', flights)
    booking_csv_save('data/bookingsdata.csv', bookings)

def main():
    print("Bienvenue dans le système de réservation de vols !")

    while True:
        choice = launch_menu()
        if choice == "1":
            show_flights()
        elif choice == "2":
            check_seats()
        elif choice == "3":
            book_flight()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Merci d'avoir utilisé notre système de réservation de vols !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
