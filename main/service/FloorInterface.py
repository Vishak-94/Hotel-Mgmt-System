from abc import abstractmethod
from main.hotel.Floor import Floor


class FloorInterface:

    @abstractmethod
    def create_floor(self, floor_id: int, corridors_dict: dict):
        raise NotImplementedError

    @abstractmethod
    def get_floor_in_str(self, floor: Floor):
        raise NotImplementedError

    @abstractmethod
    def movement_in_floor(self, floor: Floor, sub_corridor_id: int, corridor_type: str, equipment_type: str):
        raise NotImplementedError

    @abstractmethod
    def reset_floor_to_default(self, floor: Floor):
        raise NotImplementedError
