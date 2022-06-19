from main.service.SwitchInterface import SwitchInterface
from main.enums.SwitchStatus import SwitchStatus
from main.hotel.electronics.Switch import Switch


class SwitchService(SwitchInterface):

    """ Switch On Equipment """
    def switch_on(self, equipment: Switch):
        equipment.switch = SwitchStatus.ON

    """ Switch Off Equipment """
    def switch_off(self, equipment: Switch):
        equipment.switch = SwitchStatus.OFF

    """ Check Equipment Switch On  """
    def check_for_on_switch(self, equipment: Switch):
        return equipment.switch == SwitchStatus.ON

    """ Reset Equipment To Default State  """
    def reset_to_default(self, equipment: Switch):
        equipment.switch = equipment.default_state
