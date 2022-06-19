from main.constants.HotelEquipments import HotelEquipments
from main.hotel.electronics.Light import Light
from main.hotel.electronics.Ac import AC
from main.enums.SwitchStatus import SwitchStatus


class ElectronicFactory:
    @staticmethod
    def get_electrical_item_by_name(corridor_id: int, equipment_type: str, switch_status: SwitchStatus):
        if equipment_type == HotelEquipments.LIGHT:
            return Light(corridor_id, switch_status)
        elif equipment_type == HotelEquipments.AC:
            return AC(corridor_id, switch_status)
