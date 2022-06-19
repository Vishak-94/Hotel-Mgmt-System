from main.service.impl.HotelService import HotelService
from main.helper.ValidationHelper import ValidationCheck
from main.controller.InputController import InputController
from main.constants.UserMessages import UserMessages
from main.hotel.Hotel import Hotel
from main.constants.HotelBuilding import HotelBuilding
from main.constants.HotelEquipments import HotelEquipments
from time import sleep
from threading import Thread


class HotelController:
    def __init__(self):
        self.floor_count = self.movement_sub_corridor_number = self.main_corridor_count =\
            self.sub_corridor_count = self.movement_floor_number = 0
        self.default_state = True
        self.idle_time = self.default_idle_time = UserMessages.IDLE_TIME_LIMIT
        self.hotel = None
        self.__validation__ = ValidationCheck()
        self.__hotel_service__ = HotelService()
        self.__input_controller__ = InputController()
        
    '''Get Movement in Hotel From Console'''
    def get_movement_in_sub_corridor(self, hotel: Hotel):
        while True:
            print(self.__hotel_service__.get_hotel_in_str(hotel))
            self.movement_floor_number, self.movement_sub_corridor_number = \
                self.__input_controller__.get_input_movement(UserMessages.INPUT_MOVEMENT_IN_HOTEL,
                                                             UserMessages.SEPARATOR,
                                                             self.floor_count, self.sub_corridor_count)
            self.default_state = False
            Thread(target=self.start_idle_thread).start()
            self.reset_idle_time()
            self.__hotel_service__.movement_in_hotel(self.hotel,
                                                     self.movement_floor_number,
                                                     self.movement_sub_corridor_number,
                                                     HotelBuilding.SUB_CORRIDOR,
                                                     HotelEquipments.LIGHT)

    def reset_idle_time(self):
        self.idle_time = self.default_idle_time
    
    ''''Thread To Reset Hotel Equipment To Default When No Movement Is Detected'''
    def start_idle_thread(self):
        while not self.default_state:
            self.idle_time -= 1
            sleep(1)
            if self.idle_time < 0:
                self.__hotel_service__.reset_all_hotel_equipments(self.hotel)
                print(f"{UserMessages.IDLE_ALERT}")
                print(f"\n{self.__hotel_service__.get_hotel_in_str(self.hotel)}")
                print(f"{UserMessages.INPUT_MOVEMENT_IN_HOTEL}")
                self.reset_idle_time()
                self.default_state = True
    
    '''Start Main Method To Create Hotel'''
    def run_main(self):
        self.floor_count = self.__input_controller__.get_input_number(UserMessages.INPUT_FLOOR_COUNT)
        self.main_corridor_count = self.__input_controller__.get_input_number(UserMessages.INPUT_MAIN_CORRIDOR_COUNT)
        self.sub_corridor_count = self.__input_controller__.get_input_number(UserMessages.INPUT_SUB_CORRIDOR_COUNT)
        self.hotel = self.__hotel_service__.create_hotel(self.floor_count,
                                                         self.main_corridor_count,
                                                         self.sub_corridor_count)
        self.get_movement_in_sub_corridor(self.hotel)
