from main.service.FloorInterface import FloorInterface
from main.constants.HotelBuilding import HotelBuilding
from main.hotel.Floor import Floor
from main.service.impl.CorridorService import CorridorService
from main.service.impl.PowerUnitService import PowerUnitService
from main.service.impl.EquipmentService import EquipmentService


class FloorService(FloorInterface):
    __corridor_service__ = CorridorService()
    __power_unit_service__ = PowerUnitService()
    __equipment_service__ = EquipmentService()

    """ Create Floor Object For All Corridor Type """
    def create_floor(self, floor_id: int, corridors_dict: dict):
        try:
            return self.__add_corridors__(Floor(floor_id), corridors_dict)
        except Exception as exp:
            print(f"Exception in Floor Service -> create_floor {exp}")

    """ Get Floor Object With All Corridor As String """
    def get_floor_in_str(self, floor: Floor):
        try:
            floor_str = f"\t\t\t{HotelBuilding.FLOOR} {floor.floor_id}"
            for corridor in self.__corridor_service__.get_all_corridors_in_floor(floor):
                floor_str += f"\n{self.__corridor_service__.get_corridor_in_str(corridor)}"
            return floor_str
        except Exception as exp:
            print(f"Exception in Floor Service -> get_floor_in_str {exp}")

    """ Based On Movement In Corridor Switch On Light """
    def movement_in_floor(self, floor: Floor, corridor_id: int, corridor_type: str, equipment_type: str):
        try:
            self.__corridor_service__.movement_in_corridor(floor, corridor_type, corridor_id, equipment_type)
            self.__power_unit_service__.check_power_limit_in_floor(floor)
        except Exception as exception:
            print(f"Exception in Floor Service :movement_in_floor {exception}")

    """ Reset All Equipment To Default State In Floor Object """
    def reset_floor_to_default(self, floor: Floor):
        try:
            for corridor in self.__corridor_service__.get_all_corridors_in_floor(floor):
                self.__equipment_service__.reset_all_equipment_switch(corridor)
        except Exception as exp:
            print(f"Exception in Floor Service -> reset_floor_to_default {exp}")

    """ Get All Corridors In Floor """
    @staticmethod
    def get_all_corridors_in_floor(floor: Floor):
        try:
            for corr_list in floor.corridors.values():
                for corridor in corr_list:
                    yield corridor
        except Exception as exp:
            print(f"Exception in Floor Service -> get_all_corridors_in_floor {exp}")

    """ Add Corridors To Floor Object """
    def __add_corridors__(self, floor: Floor, corridors: dict):
        try:
            for corridor_type, count in corridors.items():
                self.__power_unit_service__.calculate_power_unit_in_floor(floor, corridor_type, count)
                for corridor_id in range(1, count + 1):
                    floor.corridors = self.__corridor_service__.create_corridor(corridor_id, corridor_type)
            self.__power_unit_service__.check_power_limit_in_floor(floor)
            return floor
        except Exception as exp:
            print(f"Exception in Floor Service -> __add_corridors__ {exp}")
