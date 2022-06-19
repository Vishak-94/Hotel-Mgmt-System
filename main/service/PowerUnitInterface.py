from abc import abstractmethod
from main.hotel.Floor import Floor


class PowerUnitInterface:
    @abstractmethod
    def calculate_power_unit_in_floor(self, floor: Floor, corridor_type: str, corridor_count: int):
        raise NotImplementedError

    @abstractmethod
    def check_power_limit_in_floor(self, floor: Floor):
        raise NotImplementedError
