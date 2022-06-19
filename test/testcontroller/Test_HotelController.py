from unittest import TestCase, main, TestLoader, TextTestRunner
from time import time
from re import sub, compile
from main.service.impl.HotelService import HotelService
from main.controller.HotelController import HotelController
from test.constants.TestConstants import TestConstant
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments


class TestHotelController(TestCase):
    space_pattern = compile(r'\s+')
    test_floor = 2
    test_main_corridor = 1
    test_sub_corridor = 2
    test_idle_time = 1
    test_movement_in_floor = 1
    test_movement_in_sub_corridor = 2
    hotel_controller_test = HotelController()
    hotel_service = HotelService()

    def setUp(self):
        self.hotel_controller_test.hotel = self.hotel_service.create_hotel(self.test_floor,
                                                                           self.test_main_corridor,
                                                                           self.test_sub_corridor)

    def test_hotel_switches_first_run(self):
        self.assertEqual(sub(self.space_pattern, "", TestConstant.default_object),
                         sub(self.space_pattern, "",
                             self.hotel_service.get_hotel_in_str(self.hotel_controller_test.hotel)))

    def test_hotel_movement_subcorridor(self):
        self.hotel_service.movement_in_hotel(self.hotel_controller_test.hotel,
                                             self.test_movement_in_floor,
                                             self.test_movement_in_sub_corridor,
                                             HotelBuilding.SUB_CORRIDOR,
                                             HotelEquipments.LIGHT)
        self.assertEqual(sub(self.space_pattern, "", TestConstant.movement_in_floor1_sub_corridor2),
                         sub(self.space_pattern, "",
                             self.hotel_service.get_hotel_in_str(self.hotel_controller_test.hotel)))

    def test_hotel_switch_to_default_when_idle(self):
        self.hotel_service.movement_in_hotel(self.hotel_controller_test.hotel,
                                             self.test_movement_in_floor,
                                             self.test_movement_in_sub_corridor,
                                             HotelBuilding.SUB_CORRIDOR,
                                             HotelEquipments.LIGHT)
        self.hotel_controller_test.default_state = False
        self.hotel_controller_test.idle_time = self.test_idle_time
        startTime = time()
        self.hotel_controller_test.start_idle_thread()
        actual_idle_time = time() - startTime
        self.assertGreater(actual_idle_time, self.test_idle_time)
        self.assertEqual(sub(self.space_pattern, "", TestConstant.default_object),
                         sub(self.space_pattern, "",
                             self.hotel_service.get_hotel_in_str(self.hotel_controller_test.hotel)))


suite = TestLoader().loadTestsFromTestCase(TestHotelController)
TextTestRunner(verbosity=2).run(suite)
