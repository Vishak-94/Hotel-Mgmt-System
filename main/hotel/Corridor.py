from collections import defaultdict


class Corridor:
    def __init__(self, corridor_id: int, corridor_type: str):
        self.__corridor_id = corridor_id
        self.__corridor_type = corridor_type
        self.__equipments = defaultdict(lambda: [])

    @property
    def corridor_id(self):
        return self.__corridor_id

    @property
    def corridor_type(self):
        return self.__corridor_type

    @property
    def equipments(self):
        return self.__equipments

    @equipments.setter
    def equipments(self, equipment: object):
        self.__equipments[equipment.equipment_type].append(equipment)
