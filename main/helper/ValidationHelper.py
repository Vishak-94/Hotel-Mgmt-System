from main.constants.UserMessages import UserMessages


class ValidationCheck:

    def check_movement_format(self, movement_input: list, floor_count: int, sub_corridor_count: int):
        valid_flag = False
        if len(movement_input) == 2:
            movement_floor = self.check_for_number(movement_input[0])
            if movement_floor > 0:
                movement_corridor = self.check_for_number(movement_input[1])
                if movement_corridor > 0:
                    return self.check_range_floor_and_corridor_number(movement_floor, movement_corridor,
                                                                      floor_count, sub_corridor_count)
                else:
                    print(f"{UserMessages.SUB_CORRIDOR_NOT_VALID}")
            else:
                print(f"{UserMessages.FLOOR_NOT_VALID}")
        else:
            print(f"{UserMessages.INPUT_MOVEMENT_FORMAT_INVALID}")
        return valid_flag

    def check_range_floor_and_corridor_number(self, floor_number: int, corridor_number: int, floor_count: int,
                                              sub_corridor_count: int):
        if floor_number > floor_count:
            print(f"{UserMessages.FLOOR_NOT_EXISTS}")
        elif corridor_number > sub_corridor_count:
            print(f"{UserMessages.SUB_CORRIDOR_NOT_EXISTS}")
        else:
            return True
        return False

    def check_for_number(self, number: int):
        try:
            return int(number)
        except ValueError:
            print(f"{UserMessages.NUMBER_INVALID}")
            return 0
