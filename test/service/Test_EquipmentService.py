from main.service.impl.EquipmentService import EquipmentService
from unittest import TestCase, main
from main.service.impl.CorridorService import CorridorService, HotelEquipments
from main.constants.HotelBuilding import HotelBuilding
from test.constants.TestConstants import TestConstant


class EquipmentServiceTest(TestCase):
    test_equipment_service = EquipmentService()
    test_corridor_service = CorridorService()
    test_corridor_id = 1
    test_corridor_type = HotelBuilding.SUB_CORRIDOR

    def setUp(self):
        self.corridor = self.test_corridor_service.create_corridor(self.test_corridor_id, self.test_corridor_type)

    def test_get_all_equipments_in_str(self):
        corridor_str = self.test_equipment_service.get_all_equipments_in_str(self.corridor)
        self.assertEqual(TestConstant.default_equipment_sub_corridor, corridor_str)

    def test_get_all_equipments_switch_any(self):
        equipments = self.test_equipment_service.get_all_equipments(self.corridor)
        self.assertEqual(2, len(list(equipments)))

    def test_get_all_equipments_switch_on(self):
        equipments = self.test_equipment_service.get_all_equipments(self.corridor, True)
        self.assertEqual(1, len(list(equipments)))

    def test_check_for_equip_switch_on(self):
        self.assertEqual(True, self.test_equipment_service.check_for_equipment_switch_on(self.corridor,
                                                                                         HotelEquipments.AC))

    def test_check_for_equip_switch_off(self):
        self.assertEqual(False,
                         self.test_equipment_service.check_for_equipment_switch_on(self.corridor,
                                                                                   HotelEquipments.LIGHT))

    def test_switch_off_equip(self):
        self.test_equipment_service.switch_off_equipment(self.corridor, HotelEquipments.AC)
        self.assertEqual(False,
                         self.test_equipment_service.check_for_equipment_switch_on(self.corridor,
                                                                                   HotelEquipments.AC))

    def test_switch_on_equip(self):
        self.test_equipment_service.switch_on_equipment(self.corridor, HotelEquipments.LIGHT)
        self.assertEqual(True,
                         self.test_equipment_service.check_for_equipment_switch_on(self.corridor,
                                                                                   HotelEquipments.LIGHT))

    def test_reset_all_equipment_state(self):
        self.test_equipment_service.switch_off_equipment(self.corridor, HotelEquipments.LIGHT)
        self.test_equipment_service.reset_all_equipment_switch(self.corridor)
        self.assertEqual(False,
                         self.test_equipment_service.check_for_equipment_switch_on(self.corridor,
                                                                                   HotelEquipments.LIGHT))


if __name__ == '__main__':
    main()
