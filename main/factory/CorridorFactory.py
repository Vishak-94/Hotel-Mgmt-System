from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from main.hotel.Corridor import Corridor
from main.factory.ElectronicFactory import ElectronicFactory


class CorridorFactory:

    """ Create Corridor Object Based on Corridor Type """
    def create_corridor(self, corridor_id: int, corridor_type: str):
        if corridor_type == HotelBuilding.MAIN_CORRIDOR:
            return self.__main_corridor__(corridor_id)
        elif corridor_type == HotelBuilding.SUB_CORRIDOR:
            return self.__sub_corridor__(corridor_id)
        else:
            return

    """ Create Main Corridor Object"""
    def __main_corridor__(self, corr_id: int):
        corridor_obj = Corridor(corr_id, HotelBuilding.MAIN_CORRIDOR)
        self.update_equipments_to_corridor(corridor_obj, list(self.__set_main_corridor_equipment_list__(corr_id)))
        return corridor_obj

    """ Create Sub Corridor Object"""
    def __sub_corridor__(self, corr_id: int):
        corridor_obj = Corridor(corr_id, HotelBuilding.SUB_CORRIDOR)
        self.update_equipments_to_corridor(corridor_obj, list(self.__set_sub_corridor_equipment_list__(corr_id)))
        return corridor_obj

    """ Update Equipments to Corridor Object"""
    @staticmethod
    def update_equipments_to_corridor(corridor: Corridor, all_equipments):
        for items in all_equipments:
            corridor.equipments = items

    """ Set Default Equipments to Main Corridor Object"""
    @staticmethod
    def __set_main_corridor_equipment_list__(corridor_id):
        for equipment_type, equipment_count in HotelEquipments.MAIN_CORRIDOR_EQUIPMENTS.items():
            for equipment in range(equipment_count):
                yield ElectronicFactory\
                    .get_electrical_item_by_name(corridor_id,
                                                 equipment_type,
                                                 HotelEquipments.MAIN_CORRIDOR_EQUIPMENT_STATUS[equipment_type])

    """ Set Default Equipments to Sub Corridor Object"""
    @staticmethod
    def __set_sub_corridor_equipment_list__(corridor_id):
        for equipment_type, equipment_count in HotelEquipments.SUB_CORRIDOR_EQUIPMENTS.items():
            for equipment in range(equipment_count):
                yield ElectronicFactory \
                    .get_electrical_item_by_name(corridor_id,
                                                 equipment_type,
                                                 HotelEquipments.SUB_CORRIDOR_EQUIPMENT_STATUS[equipment_type])
