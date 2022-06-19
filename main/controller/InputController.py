from main.helper.ValidationHelper import ValidationCheck


class InputController:
    __validation__ = ValidationCheck()

    def get_input_number(self, console_print_msg):
        while True:
            print(f"{console_print_msg}", end=" ")
            input_number = self.__validation__.check_for_number(input())
            if input_number > 0:
                return input_number

    def get_input_movement(self, console_print_msg, separator, *hotel_limit):
        while True:
            print(f"{console_print_msg}")
            movement_input = input().split(f"{separator}")
            if self.__validation__.check_movement_format(movement_input, hotel_limit[0], hotel_limit[1]):
                return map(lambda input_str: int(input_str), movement_input)
