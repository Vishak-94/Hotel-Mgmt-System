from unittest import TestCase, main
from main.hotel.electronics.Light import Light
from main.enums.SwitchStatus import SwitchStatus
from test.constants.TestConstants import TestConstant


class TestAC(TestCase):
    def setUp(self):
        self.light = Light(2, SwitchStatus.ON)

    def test_get_light_id(self):
        self.assertEqual(2, self.light.light_id)

    def test_get_switch_status(self):
        self.assertEqual(SwitchStatus.ON, self.light.switch)

    def test_set_switch_status(self):
        self.light.switch = SwitchStatus.OFF
        self.assertEqual(SwitchStatus.OFF, self.light.switch)

    def test_str(self):
        self.assertEqual(TestConstant.light_on, str(self.light))


if __name__ == '__main__':
    main()
