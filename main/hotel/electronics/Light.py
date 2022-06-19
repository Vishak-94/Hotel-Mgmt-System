from main.constants.HotelEquipments import HotelEquipments
from main.hotel.electronics.Switch import Switch
from enum import Enum


class Light(Switch):
    def __init__(self, light_id: int, status: Enum, power_unit=5):
        self.__light_id = light_id
        super().__init__(HotelEquipments.LIGHT, status, power_unit)

    @property
    def light_id(self):
        return self.__light_id

    def __str__(self):
        return f"{HotelEquipments.LIGHT} {self.light_id}: {self.switch.name}"
