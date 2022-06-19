from abc import abstractmethod
from main.hotel.Floor import Floor
from main.hotel.Corridor import Corridor


class CorridorInterface:
    @abstractmethod
    def create_corridor(self, corridor_id: int, corridor_type: str):
        raise NotImplementedError

    @abstractmethod
    def get_corridor_in_str(self, corridor: Corridor):
        raise NotImplementedError

    @abstractmethod
    def get_all_corridors_in_floor(self, floor: Floor):
        raise NotImplementedError

    @abstractmethod
    def movement_in_corridor(self, floor: Floor, corridor_type: str, corridor_id: int, equipment_type: str):
        raise NotImplementedError
