import unittest
from src import Flight
from src import User
from src import Booking
from src import booking_csv_save

import csv
import os

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.flight = Flight('BA001', 'Paris', 'London', 200, 200)
        self.user = User('Duval', 35)
        self.flight2 = Flight('BA002', 'Kiev', 'Moscou', 50, 50)

    def test_booking_reduce_seats(self):
        booking = Booking(self.flight, self.user, 10)
        self.flight.book(10)
        self.assertEqual(self.flight.currCapacity, 190)

    def test_cancel_increase_seats(self):
        booking = Booking(self.flight, self.user, 10)
        self.flight.book(10)
        booking.cancel(self.flight)
        self.assertEqual(self.flight.currCapacity, 200)

    def test_booking_association_user(self):
        booking = Booking(self.flight, self.user, 10)
        self.assertEqual(booking.user.name, 'Duval')
        self.assertEqual(booking.user.age, 35)

    def test_cancel_management(self):
        booking = Booking(self.flight, self.user, 10)
        self.flight.book(10)
        self.assertTrue(booking.cancel(self.flight))
        self.assertFalse(booking.cancel(self.flight2))

    def test_booking_csv_save(self):
        file_path = 'testdata.csv'
        booking = [
            Booking(
                Flight(
                    self.flight.flightid, self.flight.fromloc, self.flight.toloc, self.flight.capacity, self.flight.currCapacity),
                User(
                    self.user.name, self.user.age),
                10
            )
        ]
        booking_csv_save(file_path, booking)

        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(rows[0]['flightid'], 'BA001')
            self.assertEqual(rows[0]['fromloc'], 'Paris')
            self.assertEqual(rows[0]['toloc'], 'London')
            self.assertEqual(int(rows[0]['capacity']), 200)
            self.assertEqual(int(rows[0]['currcapacity']), 200)
            self.assertEqual(rows[0]['username'], 'Duval')
            self.assertEqual(int(rows[0]['userage']), 35)
            self.assertEqual(int(rows[0]['staff']), 10)
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
