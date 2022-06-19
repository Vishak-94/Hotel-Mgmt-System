from main.service.PowerUnitInterface import PowerUnitInterface
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from main.hotel.Floor import Floor
from main.service.impl.CorridorService import CorridorService
from main.service.impl.EquipmentService import EquipmentService


class PowerUnitService(PowerUnitInterface):
    __corridor_service__ = CorridorService()
    __equipment_service__ = EquipmentService()

    """ Calculate Total Power Consumed Based On Corridor Type  """
    def calculate_power_unit_in_floor(self, floor: Floor, corridor_type: str, corridor_count: int):
        try:
            if corridor_type == HotelBuilding.MAIN_CORRIDOR:
                self.__calculate_power_unit__(floor, corridor_count, HotelBuilding.MAIN_CORRIDOR_POWER_UNIT)

            elif corridor_type == HotelBuilding.SUB_CORRIDOR:
                self.__calculate_power_unit__(floor, corridor_count, HotelBuilding.SUB_CORRIDOR_POWER_UNIT)
        except Exception as exception:
            print(f"Exception in PowerUnit Service : calculate_power_unit_in_floor {exception}")

    """ Check For Power Limit Exceed """
    def check_power_limit_in_floor(self, floor: Floor):
        try:
            while self.__check_for_power_limit_exceed__(floor):
                if not self.__power_limit_exceed__(floor):
                    break
        except Exception as exception:
            print(f"Exception in PowerUnit Service : check_power_limit_in_floor {exception}")

    @staticmethod
    def __calculate_power_unit__(floor: Floor, corridor_count: int, power_limit: int):
        floor.power_limit += corridor_count * power_limit

    """ Check For Total Power Limit Greater Than Actual Power Unit """
    def __check_for_power_limit_exceed__(self, floor: Floor):
        return self.__current_power_unit_consumed__(floor) > floor.power_limit

    """ Calculate Current Power Unit Of Floor """
    def __current_power_unit_consumed__(self, floor: Floor):
        try:
            actual_power = 0
            for equip in self.__corridor_service__.get_all_equipment_in_corridors_switched_on(floor):
                actual_power += equip.power_unit
            return actual_power
        except Exception as exception:
            print(f"Exception in PowerUnit Service : __current_power_unit_consumed__ {exception}")

    """ Switch Off AC If Power Limit Exceeded  """
    def __power_limit_exceed__(self, floor: Floor):
        try:
            for sub_corridor in floor.corridors[HotelBuilding.SUB_CORRIDOR]:
                if self.__equipment_service__.check_for_equipment_switch_on(sub_corridor, HotelEquipments.AC):
                    self.__equipment_service__.switch_off_equipment(sub_corridor, HotelEquipments.AC)
                    return True
            return False
        except Exception as exception:
            print(f"Exception in PowerUnit Service : __power_limit_exceed__ {exception}")

