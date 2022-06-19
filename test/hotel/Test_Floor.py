from unittest import TestCase, main
from main.hotel.Floor import Floor
from main.constants.HotelBuilding import HotelBuilding
from collections import defaultdict


class TestFloor(TestCase):

    def setUp(self):
        self.floor = Floor(2)

    def test_get_floor_id(self):
        self.assertEqual(2, self.floor.floor_id)

    def test_get_power_limit(self):
        self.assertEqual(0, self.floor.power_limit)

    def test_set_power_limit(self):
        self.floor.power_limit = 15
        self.assertEqual(15, self.floor.power_limit)

    def test_set_corridor(self):
        self.floor.corridors[HotelBuilding.SUB_CORRIDOR] = 2
        self.assertEqual(2, self.floor.corridors[HotelBuilding.SUB_CORRIDOR])

    def test_get_corridor(self):
        self.assertEqual(defaultdict, type(self.floor.corridors))


if __name__ == '__main__':
    main()
