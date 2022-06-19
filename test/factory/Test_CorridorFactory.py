from unittest import TestCase, main
from main.factory.CorridorFactory import CorridorFactory
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from main.enums.SwitchStatus import SwitchStatus


class TestCorridorFactory(TestCase):
    corridor_factory = CorridorFactory()
    test_corridor_id = 2

    def test_main_corridor_light_on_ac_on(self):
        corridor = self.corridor_factory.create_corridor(self.test_corridor_id, HotelBuilding.MAIN_CORRIDOR)
        self.assertEqual(HotelBuilding.MAIN_CORRIDOR, corridor.corridor_type)
        self.assertEqual(SwitchStatus.ON, corridor.equipments[HotelEquipments.LIGHT][0].switch)
        self.assertEqual(SwitchStatus.ON, corridor.equipments[HotelEquipments.AC][0].switch)
        self.assertEqual(self.test_corridor_id, corridor.corridor_id)

    def test_sub_corridor_light_off_ac_on(self):
        corridor = self.corridor_factory.create_corridor(self.test_corridor_id, HotelBuilding.SUB_CORRIDOR)
        self.assertEqual(HotelBuilding.SUB_CORRIDOR, corridor.corridor_type, )
        self.assertEqual(SwitchStatus.OFF, corridor.equipments[HotelEquipments.LIGHT][0].switch)
        self.assertEqual(SwitchStatus.ON, corridor.equipments[HotelEquipments.AC][0].switch)
        self.assertEqual(self.test_corridor_id, corridor.corridor_id)


if __name__ == "__main__":
    main()
