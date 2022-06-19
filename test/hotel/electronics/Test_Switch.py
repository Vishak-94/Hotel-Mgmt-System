from unittest import TestCase, main
from main.hotel.electronics.Switch import Switch
from main.enums.SwitchStatus import SwitchStatus
from main.constants.HotelEquipments import HotelEquipments


class TestSwitch(TestCase):
    def setUp(self):
        self.switch = Switch(HotelEquipments.AC, SwitchStatus.ON, 15)

    def test_get_equipment_type(self):
        self.assertEqual(HotelEquipments.AC, self.switch.equipment_type)

    def test_get_switch_status(self):
        self.assertEqual(SwitchStatus.ON, self.switch.switch)

    def test_set_switch_status(self):
        self.switch.switch = SwitchStatus.OFF
        self.assertEqual(SwitchStatus.OFF, self.switch.switch)

    def test_get_power_unit(self):
        self.assertEqual(15, self.switch.power_unit)

    def test_str(self):
        self.assertEqual(SwitchStatus.ON.name, str(self.switch))


if __name__ == '__main__':
    main()
