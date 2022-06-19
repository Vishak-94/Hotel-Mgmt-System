from unittest import TestCase, main
from main.service.impl.FloorService import FloorService
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from main.hotel.Floor import Floor
from re import sub, compile
from test.constants.TestConstants import TestConstant
from main.service.impl.EquipmentService import EquipmentService
from main.service.impl.CorridorService import CorridorService


class TestFloorService(TestCase):
    test_floor_service = FloorService()
    test_equipment_service = EquipmentService()
    test_corridor_service = CorridorService()
    test_floor_id = 1
    space_pattern = compile(r'\s+')

    def setUp(self):
        self.test_floor = self.test_floor_service.create_floor(
            self.test_floor_id,
            {HotelBuilding.MAIN_CORRIDOR: 1, HotelBuilding.SUB_CORRIDOR: 2})

    def test_create_floor(self):
        self.assertEqual(Floor, type(self.test_floor))

    def test_get_floor_in_str(self):
        self.assertEqual(sub(self.space_pattern, "", TestConstant.default_floor1_str),
            sub(self.space_pattern, "", self.test_floor_service.get_floor_in_str(self.test_floor)))

    def test_movement_in_floor(self):
        self.test_floor_service.movement_in_floor(self.test_floor, 1, HotelBuilding.SUB_CORRIDOR, HotelEquipments.LIGHT)
        corridor = self.test_corridor_service.get_corridor(self.test_floor, HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(True,
                         self.test_equipment_service.check_for_equipment_switch_on(corridor, HotelEquipments.LIGHT))

    def test_reset_floor_to_default(self):
        self.test_floor_service.movement_in_floor(self.test_floor, 1, HotelBuilding.SUB_CORRIDOR, HotelEquipments.LIGHT)
        self.test_floor_service.reset_floor_to_default(self.test_floor)
        corridor = self.test_corridor_service.get_corridor(self.test_floor, HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(False,
                         self.test_equipment_service.check_for_equipment_switch_on(corridor, HotelEquipments.LIGHT))

    def test_get_all_corridors_in_floor(self):
        corridor_generator = self.test_floor_service.get_all_corridors_in_floor(self.test_floor)
        self.assertEqual(3, len(list(corridor_generator)))


if __name__ == '__main__':
    main()
