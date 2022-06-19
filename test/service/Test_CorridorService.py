from unittest import TestCase, main
from test.constants.TestConstants import TestConstant
from main.service.impl.CorridorService import CorridorService
from main.service.impl.EquipmentService import EquipmentService
from main.service.impl.HotelService import HotelService
from main.service.impl.FloorService import FloorService
from main.constants.HotelBuilding import HotelBuilding
from collections import defaultdict
from main.constants.HotelEquipments import HotelEquipments


class CorridorServiceTest(TestCase):
    test_corridor_service = CorridorService()
    test_equipment_service = EquipmentService()
    test_hotel_service = HotelService()
    test_floor_service = FloorService()
    test_corridor_id = 1
    test_floor_count = 1
    test_default_equipment_count = 3
    test_default_corridor_count = 2

    def test_create_corridor(self):
        corridor = self.test_corridor_service.create_corridor(self.test_corridor_id, HotelBuilding.SUB_CORRIDOR)
        self.assertEqual(corridor.corridor_type, HotelBuilding.SUB_CORRIDOR)
        self.assertEqual(corridor.corridor_id, self.test_corridor_id)
        self.assertEqual(defaultdict, type(corridor.equipments))

    def test_get_corridor_in_str(self):
        corridor = self.test_corridor_service.create_corridor(self.test_corridor_id, HotelBuilding.SUB_CORRIDOR)
        corridor_str = self.test_corridor_service.get_corridor_in_str(corridor)
        self.assertEqual(TestConstant.sub_corridor_default, corridor_str)

    def test_movement_in_corridor(self):
        floor = self.get_floor_object()
        self.test_corridor_service.movement_in_corridor(floor, HotelBuilding.SUB_CORRIDOR, 1, HotelEquipments.LIGHT)
        self.assertEqual(TestConstant.sub_corridor_light_on,
                         self.test_corridor_service.get_corridor_in_str(floor.corridors[HotelBuilding.SUB_CORRIDOR][0]))

    def test_get_all_equipment_in_corridors_switched_on(self):
        floor = self.get_floor_object()
        self.assertEqual(self.test_default_equipment_count,
                         len(list(self.test_corridor_service.get_all_equipment_in_corridors_switched_on(floor))))

    def test_get_all_corridors_in_floor(self):
        floor = self.get_floor_object()
        self.assertEqual(self.test_default_corridor_count,
                         len(list(self.test_corridor_service.get_all_corridors_in_floor(floor))))

    def test_get_corridor(self):
        floor = self.get_floor_object()
        corridor = self.test_corridor_service.get_corridor(floor, HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(TestConstant.sub_corridor_default, self.test_corridor_service.get_corridor_in_str(corridor))

    def get_floor_object(self):
        return self.test_floor_service.create_floor(self.test_floor_count, self.get_corridor_dict())

    @staticmethod
    def get_corridor_dict():
        return {HotelBuilding.MAIN_CORRIDOR: 1, HotelBuilding.SUB_CORRIDOR: 1}


if __name__ == '__main__':
    main()
