from main.constants.HotelEquipments import HotelEquipments
from main.hotel.electronics.Switch import Switch
from main.enums.SwitchStatus import SwitchStatus


class AC(Switch):
    def __init__(self, ac_id: int, status: SwitchStatus, power_unit=10):
        self.__ac_id = ac_id
        super().__init__(HotelEquipments.AC, status, power_unit)

    @property
    def ac_id(self):
        return self.__ac_id

    def __str__(self):
        return f"{HotelEquipments.AC}: {self.switch.name}"
