from main.service.impl.SwitchService import SwitchService
from main.enums.SwitchStatus import SwitchStatus
from unittest import TestCase, main
from main.hotel.electronics.Switch import Switch
from main.constants.HotelEquipments import HotelEquipments


class SwitchServiceTest(TestCase):
    test_switch_service = SwitchService()
    test_power_unit = 10

    def test_switch_on(self):
        equipment = Switch(HotelEquipments.LIGHT, SwitchStatus.OFF, self.test_power_unit)
        self.test_switch_service.switch_on(equipment)
        self.assertEqual(SwitchStatus.ON, equipment.switch)

    def test_switch_off(self):
        equipment = Switch(HotelEquipments.LIGHT, SwitchStatus.ON, self.test_power_unit)
        self.test_switch_service.switch_off(equipment)
        self.assertEqual(SwitchStatus.OFF, equipment.switch)

    def test_check_for_on_switch(self):
        equipment = Switch(HotelEquipments.LIGHT, SwitchStatus.ON, self.test_power_unit)
        self.assertEqual(True, self.test_switch_service.check_for_on_switch(equipment))

    def test_reset_to_default(self):
        equipment = Switch(HotelEquipments.LIGHT, SwitchStatus.OFF, self.test_power_unit)
        self.test_switch_service.switch_on(equipment)
        self.test_switch_service.reset_to_default(equipment)
        self.assertEqual(SwitchStatus.OFF, equipment.switch)


if __name__ == '__main__':
    main()
