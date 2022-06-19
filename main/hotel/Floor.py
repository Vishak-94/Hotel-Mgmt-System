from main.hotel.Corridor import Corridor
from collections import defaultdict


class Floor:
    def __init__(self, floor_id: int):
        self.__floor_id = floor_id
        self.__corridors = defaultdict(lambda: [])
        self.__power_limit = 0

    @property
    def power_limit(self):
        return self.__power_limit

    @power_limit.setter
    def power_limit(self, power_limit: int):
        self.__power_limit = power_limit

    @property
    def floor_id(self):
        return self.__floor_id

    @property
    def corridors(self):
        return self.__corridors

    @corridors.setter
    def corridors(self, corridor: Corridor):
        self.__corridors[corridor.corridor_type].append(corridor)
