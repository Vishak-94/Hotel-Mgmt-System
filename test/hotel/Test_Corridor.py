from unittest import TestCase, main
from main.hotel.Corridor import Corridor
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from collections import defaultdict


class TestCorridor(TestCase):
    def setUp(self):
        self.corridor = Corridor(2, HotelBuilding.SUB_CORRIDOR)

    def test_get_corridor_id(self):
        self.assertEqual(2, self.corridor.corridor_id)

    def test_get_corridor_type(self):
        self.assertEqual(HotelBuilding.SUB_CORRIDOR, self.corridor.corridor_type)

    def test_get_equipments(self):
        self.assertEqual(defaultdict, type(self.corridor.equipments))

    def test_set_equipments(self):
        self.corridor.equipments[HotelEquipments.LIGHT] = 2
        self.assertEqual(2, self.corridor.equipments[HotelEquipments.LIGHT])


if __name__ == '__main__':
    main()
