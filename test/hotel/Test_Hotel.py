from unittest import TestCase, main
from main.service.impl.HotelService import HotelService
from main.hotel.Hotel import Hotel
from main.hotel.Floor import Floor


class TestHotel(TestCase):
    hotel_service = HotelService()
    test_sub_corridor_count = 2
    test_main_corridor_count = 1

    def setUp(self):
        self.test_floor_count = 2

    def test_null_floor(self):
        self.hotel = Hotel(self.test_floor_count)
        self.assertEqual(self.hotel.floors, [])

    def test_hotel_floor_count(self):
        hotel = self.hotel_service.create_hotel(self.test_floor_count,
                                                self.test_main_corridor_count,
                                                self.test_sub_corridor_count)
        self.assertEqual(len(hotel.floors), self.test_floor_count)

    def test_floor_getter(self):
        self.hotel = Hotel(self.test_floor_count)
        self.hotel.floors = Floor(self.test_floor_count)
        self.assertEqual(len(self.hotel.floors), 1)


if __name__ == '__main__':
    main()
