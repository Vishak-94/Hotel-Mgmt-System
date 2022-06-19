from unittest import TestCase, main
from main.constants.HotelEquipments import HotelEquipments
from main.service.impl.PowerUnitService import PowerUnitService
from main.service.impl.CorridorService import CorridorService
from main.service.impl.HotelService import HotelService
from main.constants.HotelBuilding import HotelBuilding
from main.service.impl.EquipmentService import EquipmentService


class PowerUnitServiceTest(TestCase):
    test_power_unit_service = PowerUnitService()
    test_hotel_service = HotelService()
    test_corridor_service = CorridorService()
    test_equipment_service = EquipmentService()
    test_floor_count = 2
    test_main_corridor_count = 1
    test_sub_corridor_count = 2

    def setUp(self):
        self.test_hotel = self.test_hotel_service.create_hotel(self.test_floor_count,
                                                               self.test_main_corridor_count,
                                                               self.test_sub_corridor_count)

    def test_calculate_power_unit_in_floor(self):
        self.assertEqual(35, self.test_hotel.floors[0].power_limit)

    def test_check_power_limit_in_floor_Exceeded(self):
        self.test_hotel_service.movement_in_hotel(self.test_hotel, 1, 2,
                                                  HotelBuilding.SUB_CORRIDOR, HotelEquipments.LIGHT)
        corridor = self.test_corridor_service.get_corridor(self.test_hotel.floors[0],
                                                           HotelBuilding.SUB_CORRIDOR, 1)
        self.assertEqual(False, self.test_equipment_service.check_for_equipment_switch_on(corridor,
                                                                                          HotelEquipments.AC))

    def test_check_power_limit_in_floor_Not_Exceeded(self):
        self.test_hotel_service.movement_in_hotel(self.test_hotel, 1, 2,
                                                  HotelBuilding.SUB_CORRIDOR, HotelEquipments.LIGHT)
        self.test_hotel_service.movement_in_hotel(self.test_hotel, 1, 1,
                                                  HotelBuilding.SUB_CORRIDOR, HotelEquipments.LIGHT)
        corridor = self.test_corridor_service.get_corridor(self.test_hotel.floors[0],
                                                           HotelBuilding.SUB_CORRIDOR, 2)
        self.assertEqual(True, self.test_equipment_service.check_for_equipment_switch_on(corridor,
                                                                                         HotelEquipments.AC))


if __name__ == "__main__":
    main()
