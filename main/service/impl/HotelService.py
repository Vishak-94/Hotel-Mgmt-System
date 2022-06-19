from main.service.HotelInterface import HotelInterface
from main.hotel.Hotel import Hotel
from main.service.impl.FloorService import FloorService
from main.constants.HotelBuilding import HotelBuilding


class HotelService(HotelInterface):
    __floor_service__ = FloorService()

    """ Create Hotel Object With Corridor Count """
    def create_hotel(self, floor_count: int, main_corridor_count: int, sub_corridor_count: int):
        try:
            hotel = Hotel(floor_count)
            corridor_dict = self.map_corridor_to_dict(main_corridor_count, sub_corridor_count)
            for floor_id in range(1, floor_count + 1):
                hotel.floors = self.__floor_service__.create_floor(floor_id, corridor_dict)
            return hotel
        except Exception as exp:
            print(f"Exception in Hotel Service -> create_hotel {exp}")

    """ Get Hotel Object In Str """
    def get_hotel_in_str(self, hotel: Hotel):
        try:
            return "\n".join([self.__floor_service__.get_floor_in_str(floor) for floor in hotel.floors])
        except Exception as exp:
            print(f"Exception in Hotel Service -> get_hotel_in_str {exp}")

    """ Switch On Equipment In Hotel For Movement In Corridor """
    def movement_in_hotel(self, hotel: Hotel, floor_id: int, corridor_id: int, corridor_type: str, equipment_type: str):
        try:
            self.__floor_service__.movement_in_floor(hotel.floors[floor_id - 1],
                                                     corridor_id, corridor_type, equipment_type)
        except Exception as exception:
            print(f"Exception in Hotel Service : movement_in_hotel {exception}")

    """ Reset All Equipment To Default State For Hotel Object """
    def reset_all_hotel_equipments(self, hotel: Hotel):
        try:
            for floor in hotel.floors:
                self.__floor_service__.reset_floor_to_default(floor)
        except Exception as exception:
            print(f"Exception in Hotel Service : reset_all_hotel_equipments {exception}")

    """ Convert Corridor Count To Dict With Corridor Type """
    @staticmethod
    def map_corridor_to_dict(main_corridor_count, sub_corridor_count):
        return {HotelBuilding.MAIN_CORRIDOR: main_corridor_count,
                HotelBuilding.SUB_CORRIDOR: sub_corridor_count}
