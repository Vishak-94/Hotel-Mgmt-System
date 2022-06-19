from abc import abstractmethod
from main.hotel.electronics.Switch import Switch


class SwitchInterface:
    @abstractmethod
    def switch_on(self, equipment: Switch):
        raise NotImplementedError

    @abstractmethod
    def switch_off(self, equipment: Switch):
        raise NotImplementedError

    @abstractmethod
    def check_for_on_switch(self, equipment: Switch):
        raise NotImplementedError

    @abstractmethod
    def reset_to_default(self, equipment: Switch):
        raise NotImplementedError
