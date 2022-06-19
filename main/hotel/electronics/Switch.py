from enum import Enum


class Switch:
    def __init__(self, equipment: str, status: Enum, power_unit: int):
        self.__equipment_type = equipment
        self.__switch = status
        self.__default_state = status
        self.__power_unit = power_unit

    @property
    def equipment_type(self):
        return self.__equipment_type

    @property
    def default_state(self):
        return self.__default_state

    @property
    def power_unit(self):
        return self.__power_unit

    @property
    def switch(self):
        return self.__switch

    @switch.setter
    def switch(self, status: Enum):
        self.__switch = status

    def __str__(self):
        return self.switch.name
