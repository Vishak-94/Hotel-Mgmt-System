

class Hotel:
    def __init__(self, floor_count: int):
        self.__no_of_floor = floor_count
        self.__floors = []

    @property
    def no_of_floor(self):
        return self.__no_of_floor

    @no_of_floor.setter
    def no_of_floor(self, no_of_floor: int):
        self.__no_of_floor = no_of_floor

    @property
    def floors(self):
        return self.__floors

    @floors.setter
    def floors(self, floor: int):
        self.__floors.append(floor)
