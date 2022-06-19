from main.service.EquipmentInterface import EquipmentInterface
from main.hotel.Corridor import Corridor
from main.service.impl.SwitchService import SwitchService


class EquipmentService(EquipmentInterface):
    __switch_service__ = SwitchService()

    """Get all Equipments In Corridor In String"""
    def get_all_equipments_in_str(self, corridor: Corridor):
        try:
            return " ".join(map(lambda equip: str(equip), self.get_all_equipments(corridor)))
        except Exception as exp:
            print(f"Exception in Equipment Service -> get_all_equipments_in_str {exp}")

    """Get all Equipments In Corridor [Switch On-> Optional]"""
    def get_all_equipments(self, corridor: Corridor, switch_on=False):
        try:
            for equipment_list in corridor.equipments.values():
                for equipment in equipment_list:
                    if switch_on:
                        if self.__switch_service__.check_for_on_switch(equipment):
                            yield equipment
                    else:
                        yield equipment
        except Exception as exp:
            print(f"Exception in Equipment Service -> get_all_equipments {exp}")

    """Check For Equipment Switch On For Corridor Object"""
    def check_for_equipment_switch_on(self, corridor: Corridor, equipment_type: str, equip_id=0):
        try:
            return self.__switch_service__.check_for_on_switch(corridor.equipments[equipment_type][equip_id])
        except Exception as exp:
            print(f"Exception in Equipment Service -> check_for_equipment_switch_on {exp}")

    """Switch Off Equipment For Corridor Object"""
    def switch_off_equipment(self, corridor: Corridor, equipment_type: str, equip_id=0):
        try:
            self.__switch_service__.switch_off(corridor.equipments[equipment_type][equip_id])
        except Exception as exp:
            print(f"Exception in Equipment Service -> switch_off_equipment {exp}")

    """Switch On Equipment For Corridor Object"""
    def switch_on_equipment(self, corridor: Corridor, equipment_type: str, equip_id=0):
        try:
            self.__switch_service__.switch_on(corridor.equipments[equipment_type][equip_id])
        except Exception as exp:
            print(f"Exception in Equipment Service -> switch_on_equipment {exp}")

    """Reset Switch to Default For All Equipments In Corridor Object"""
    def reset_all_equipment_switch(self, corridor: Corridor):
        try:
            for equip in self.get_all_equipments(corridor):
                self.__switch_service__.reset_to_default(equip)
        except Exception as exp:
            print(f"Exception in Equipment Service -> reset_all_equipment_switch {exp}")
