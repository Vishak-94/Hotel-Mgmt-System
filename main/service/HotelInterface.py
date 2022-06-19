from abc import abstractmethod
from main.hotel.Hotel import Hotel


class HotelInterface:
    @abstractmethod
    def create_hotel(self, floor_count: int, main_corridor_count: int, sub_corridor_count: int):
        raise NotImplementedError

    @abstractmethod
    def get_hotel_in_str(self, hotel: Hotel):
        raise NotImplementedError

    @abstractmethod
    def movement_in_hotel(self, hotel: Hotel, floor_id: int, corridor_id: int, corridor_type: str, equipment_type: str):
        raise NotImplementedError

    @abstractmethod
    def reset_all_hotel_equipments(self, hotel: Hotel):
        raise NotImplementedError
