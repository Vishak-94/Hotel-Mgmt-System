from main.service.CorridorInterface import CorridorInterface
from main.hotel.Floor import Floor
from main.hotel.Corridor import Corridor
from main.service.impl.EquipmentService import EquipmentService
from main.factory.CorridorFactory import CorridorFactory


class CorridorService(CorridorInterface):
    __equipment_service__ = EquipmentService()
    __corridor_factory__ = CorridorFactory()

    """Creates New Corridor Object"""
    def create_corridor(self, corridor_id: int, corridor_type: str):
        try:
            return self.__corridor_factory__.create_corridor(corridor_id, corridor_type)
        except Exception as exp:
            print(f"Exception in CorridorService -> create_corridor {exp}")

    """Get Corridor Object In String Format"""
    def get_corridor_in_str(self, corridor: Corridor):
        try:
            return f"{corridor.corridor_type} {corridor.corridor_id}" \
                   f" {self.__equipment_service__.get_all_equipments_in_str(corridor)}"
        except Exception as exp:
            print(f"Exception in CorridorService -> get_corridor_in_str {exp}")

    """Change Switch State of Equipment For Floor Object"""
    def movement_in_corridor(self, floor: Floor, corridor_type: str,
                             corridor_id: int, equipment_type: str):
        try:
            self.__equipment_service__.switch_on_equipment(
                self.get_corridor(floor, corridor_type, corridor_id), equipment_type)
        except Exception as exp:
            print(f"Exception in Corridor Service -> movement_in_sub_corridor {exp}")

    """Get All Equipments With Switch On For Floor Object"""
    def get_all_equipment_in_corridors_switched_on(self, floor: Floor):
        try:
            for corridor in self.get_all_corridors_in_floor(floor):
                for equipment in self.__equipment_service__.get_all_equipments(corridor, True):
                    yield equipment
        except Exception as exp:
            print(f"Exception in Corridor Service -> get_all_equipment_in_corridors_switched_on {exp}")

    """Get All Corridor In Floor Object"""
    def get_all_corridors_in_floor(self, floor: Floor):
        try:
            for corr_list in floor.corridors.values():
                for corridor in corr_list:
                    yield corridor
        except Exception as exp:
            print(f"Exception in Corridor Service -> get_all_corridors_in_floor {exp}")

    """Get Corridor Object Based on Corridor Type and Corridor Id In Floor Object"""
    @staticmethod
    def get_corridor(floor: Floor, corridor_type: str, corridor_id: int):
        try:
            return floor.corridors[corridor_type][corridor_id - 1]
        except Exception as exp:
            print(f"Exception in Corridor Service -> get_corridor {exp}")
