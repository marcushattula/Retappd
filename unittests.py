import unittest
from datetime import date, time

from beer import Beer
from brewery import Brewery
from check_in import Check_In
from user import User
from location import Location, Address

# Confidential names/addresses
from confidentials import * 

class testAddressClass(unittest.TestCase):

    def test_place_init(self):
        testPlace1 = Address("Finland", "Uusimaa", "Kerava", "Sinebrychoffinaukio 1")

class testLocationClass(unittest.TestCase):

    def test_location_init(self):
        testPlace1 = Address("Finland", "Uusimaa", "Espoo", "Otakaari 22")
        testLocation = Location("Täffä", testPlace1, ["College Cafeteria", "Fraternity House"])

class TestBreweryClass(unittest.TestCase):

    def test_brewery_init(self):
        testPlace1 = Address("Finland", "Pohjois-Savo", "Iisalmi", "Luuniementie 6")
        testBrewery1 = Brewery("Olvi", testPlace1, 1878, None)

class TestBeerClass(unittest.TestCase):

    def test_beer_init(self):
        testPlace1 = Address("Finland", "Uusimaa", "Kerava", "Sinebrychoffinaukio 1")
        testBrewery1 = Brewery("Finland", testPlace1, 1819, None)
        testBeer1 = Beer("Karhu III", "Lager", "Pale", testBrewery1, 4.6, 16)

class TestUserClass(unittest.TestCase):

    def test_user_init(self):
        testUser = User("TheMacke", THEMACKE_NAME, 0)

class TestCheckInClass(unittest.TestCase):

    def test_checkin_init(self):
        checkin_date = date(2025, 6, 14)
        checkin_time = time(16, 41)

        testPlace1 = Address("Finland", "Uusimaa", "Nurmijärvi", HOME_ADDRESS1)
        testLocation = Location("Klake", testPlace1, ["Home"])
        testPlace2 = Address("Japan", "Tokyo", "Sumida-ku", "1-23-1 Azumabashi")
        testBrewery = Brewery("Asahi Breweries", testPlace2, 1949, None)
        testBeer = Beer("Asahi Super Dry", "Lager", "Pale", testBrewery, 5, 20)
        testUser1 = User("TheMacke", THEMACKE_NAME, 0)
        testUser2 = User("eemsue", EEMSUE_NAME, 1)
        testCheckIn = Check_In(testUser1, testBeer, 3.5, ["Light Bodied"], testLocation, [testUser2], checkin_date, checkin_time)

if __name__ == '__main__':
    unittest.main()
