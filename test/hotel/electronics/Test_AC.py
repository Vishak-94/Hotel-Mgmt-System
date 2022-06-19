from unittest import TestCase, main
from main.hotel.electronics.Ac import AC
from main.enums.SwitchStatus import SwitchStatus
from test.constants.TestConstants import TestConstant


class TestAC(TestCase):
    def setUp(self):
        self.ac = AC(2, SwitchStatus.ON)

    def test_get_ac_id(self):
        self.assertEqual(2, self.ac.ac_id)

    def test_get_switch_status(self):
        self.assertEqual(SwitchStatus.ON, self.ac.switch)

    def test_set_switch_status(self):
        self.ac.switch = SwitchStatus.OFF
        self.assertEqual(SwitchStatus.OFF, self.ac.switch)

    def test_str(self):
        self.assertEqual(TestConstant.ac_on, str(self.ac))


if __name__ == '__main__':
    main()
