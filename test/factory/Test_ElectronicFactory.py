from unittest import TestCase, main
from main.factory.ElectronicFactory import ElectronicFactory
from main.constants.HotelEquipments import HotelEquipments
from main.enums.SwitchStatus import SwitchStatus


class TestElectronicFactory(TestCase):
    electronic_factory = ElectronicFactory
    test_id = 1

    def test_light_equipment_on(self):
        equipment = self.electronic_factory.get_electrical_item_by_name(self.test_id, HotelEquipments.LIGHT,
                                                                        SwitchStatus.ON)
        self.assertEqual(SwitchStatus.ON, equipment.switch)
        self.assertEqual(self.test_id, equipment.light_id)

    def test_light_equipment_off(self):
        equipment = self.electronic_factory.get_electrical_item_by_name(self.test_id,
                                                                        HotelEquipments.LIGHT,
                                                                        SwitchStatus.OFF)
        self.assertEqual(SwitchStatus.OFF, equipment.switch)
        self.assertEqual(self.test_id, equipment.light_id)

    def test_ac_equipment_on(self):
        equipment = self.electronic_factory.get_electrical_item_by_name(self.test_id,
                                                                        HotelEquipments.AC,
                                                                        SwitchStatus.ON)
        self.assertEqual(SwitchStatus.ON, equipment.switch)
        self.assertEqual(self.test_id, equipment.ac_id)

    def test_ac_equipment_off(self):
        equipment = self.electronic_factory.get_electrical_item_by_name(self.test_id,
                                                                        HotelEquipments.AC,
                                                                        SwitchStatus.OFF)
        self.assertEqual(SwitchStatus.OFF, equipment.switch)
        self.assertEqual(self.test_id, equipment.ac_id)

    def test_none_equipment_off(self):
        equipment = self.electronic_factory.get_electrical_item_by_name(self.test_id,
                                                                        "Test_equip", SwitchStatus.ON)
        self.assertEqual(None, equipment)


if __name__ == "__main__":
    main()
