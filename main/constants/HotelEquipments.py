from main.enums.SwitchStatus import SwitchStatus


class HotelEquipments:
    LIGHT = "Light"
    AC = "AC"
    MAIN_CORRIDOR_EQUIPMENTS = {LIGHT: 1, AC: 1}
    SUB_CORRIDOR_EQUIPMENTS = {LIGHT: 1, AC: 1}
    MAIN_CORRIDOR_EQUIPMENT_STATUS = {LIGHT: SwitchStatus.ON, AC: SwitchStatus.ON}
    SUB_CORRIDOR_EQUIPMENT_STATUS = {LIGHT: SwitchStatus.OFF, AC: SwitchStatus.ON}
