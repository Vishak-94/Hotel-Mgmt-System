from abc import abstractmethod
from main.hotel.Corridor import Corridor


class EquipmentInterface:
    @abstractmethod
    def get_all_equipments(self, corridor: Corridor, switch_on: bool):
        raise NotImplementedError

    @abstractmethod
    def get_all_equipments_in_str(self, corridor: Corridor):
        raise NotImplementedError

    @abstractmethod
    def check_for_equipment_switch_on(self, corridor: Corridor, equipment: str, equip_id: int):
        raise NotImplementedError

    @abstractmethod
    def switch_off_equipment(self, corridor: Corridor, equipment: str, equip_id: int):
        raise NotImplementedError

    @abstractmethod
    def switch_on_equipment(self, corridor: Corridor, equipment: str, equip_id: int):
        raise NotImplementedError

    @abstractmethod
    def reset_all_equipment_switch(self, corridor: Corridor):
        raise NotImplementedError
