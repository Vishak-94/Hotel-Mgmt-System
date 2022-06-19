from unittest import TestCase, main
from main.helper.ValidationHelper import ValidationCheck


class ValidationCheckTest(TestCase):
    validation_check = ValidationCheck()

    def test_invalid_number_string(self):
        self.assertEqual(0, self.validation_check.check_for_number("Test"))

    def test_valid_number(self):
        self.assertGreater(self.validation_check.check_for_number("2"), 0)

    def test_movement_string_valid(self):
        self.assertEqual(True, self.validation_check.check_movement_format("2:1".split(":"), 2, 2))

    def test_movement_string_invalid(self):
        self.assertEqual(False, self.validation_check.check_movement_format("2-1".split(":"), 2, 2))

    def test_movement_floor_not_exists(self):
        self.assertEqual(False, self.validation_check.check_movement_format("3:1".split(":"), 2, 2))

    def test_movement_subcorridor_not_exists(self):
        self.assertEqual(False, self.validation_check.check_movement_format("2:3".split(":"), 2, 2))

    def test_invalid_floor_number(self):
        self.assertEqual(False, self.validation_check.check_movement_format("2:3".split(":"), -1, 2))

    def test_invalid_sub_corridor_number(self):
        self.assertEqual(False, self.validation_check.check_movement_format("2:3".split(":"), 2, -1))


if __name__ == "__main__":
    main()
