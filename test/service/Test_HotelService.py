from unittest import TestCase, main
from main.service.impl.HotelService import HotelService
from main.hotel.Hotel import Hotel
from main.service.impl.FloorService import FloorService
from main.service.impl.CorridorService import CorridorService
from main.service.impl.EquipmentService import EquipmentService
from re import sub, compile
from test.constants.TestConstants import TestConstant
from main.constants.HotelEquipments import HotelEquipments
from main.constants.HotelBuilding import HotelBuilding


class TestHotelService(TestCase):
    test_hotel_service = HotelService()
    test_floor_service = FloorService()
    test_corridor_service = CorridorService()
    test_equipment_service = EquipmentService()
    space_pattern = compile(r'\s+')
    test_floor_movement = 1
    test_sub_corridor_movement = 1
    test_floor_count = 2
    test_main_corridor_count = 1
    test_sub_corridor_count = 2

    def setUp(self):
        self.test_hotel = self.test_hotel_service.create_hotel(self.test_floor_count,
                                                               self.test_main_corridor_count,
                                                               self.test_sub_corridor_count)

    def test_create_hotel(self):
        self.assertEqual(type(self.test_hotel), Hotel)
        self.assertEqual(len(self.test_hotel.floors), self.test_floor_count)
        corridors_generator = self.test_floor_service.get_all_corridors_in_floor(self.test_hotel.floors[0])
        self.assertEqual(self.test_sub_corridor_count + self.test_main_corridor_count, len(list(corridors_generator)))

    def test_get_hotel_in_str(self):
        self.assertEqual(sub(self.space_pattern, "", TestConstant.default_object),
                         sub(self.space_pattern, "", self.test_hotel_service.get_hotel_in_str(self.test_hotel)))

    def test_movement_in_hotel(self):
        self.test_hotel_service.movement_in_hotel(self.test_hotel,
                                                  self.test_floor_movement,
                                                  self.test_sub_corridor_movement,
                                                  HotelBuilding.SUB_CORRIDOR,
                                                  HotelEquipments.LIGHT)
        corridor = self.test_corridor_service.get_corridor(self.test_hotel.floors[self.test_floor_movement - 1],
                                                           HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(True,
                         self.test_equipment_service.check_for_equipment_switch_on(corridor,
                                                                                   HotelEquipments.LIGHT))

    def test_reset_all_hotel_equipments(self):
        self.test_hotel_service.movement_in_hotel(self.test_hotel,
                                                  self.test_floor_movement,
                                                  self.test_sub_corridor_movement,
                                                  HotelBuilding.SUB_CORRIDOR,
                                                  HotelEquipments.LIGHT)
        self.test_hotel_service.reset_all_hotel_equipments(self.test_hotel)
        corridor = self.test_corridor_service.get_corridor(self.test_hotel.floors[self.test_floor_movement - 1],
                                                           HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(False, self.test_equipment_service.check_for_equipment_switch_on(corridor,
                                                                                          HotelEquipments.LIGHT))

    def test_map_corridor_to_dict(self):
        corridor_dict = self.test_hotel_service.map_corridor_to_dict(self.test_main_corridor_count,
                                                                     self.test_sub_corridor_count)
        self.assertEqual(dict, type(corridor_dict))
        self.assertEqual(self.test_main_corridor_count, corridor_dict[HotelBuilding.MAIN_CORRIDOR])
        self.assertEqual(self.test_sub_corridor_count, corridor_dict[HotelBuilding.SUB_CORRIDOR])


if __name__ == "__main__":
    main()
