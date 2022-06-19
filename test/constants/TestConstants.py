class TestConstant:

    default_floor1_str = "			    Floor 1\
                        Main Corridor 1 Light 1: ON AC: ON\
                        Sub Corridor 1 Light 1: OFF AC: ON\
                        Sub Corridor 2 Light 2: OFF AC: ON"

    default_object = f"	{default_floor1_str}\
                                    Floor 2\
                        Main Corridor 1 Light 1: ON AC: ON\
                        Sub Corridor 1 Light 1: OFF AC: ON\
                        Sub Corridor 2 Light 2: OFF AC: ON"

    movement_in_floor1_sub_corridor2 = "			Floor 1\
                                        Main Corridor 1 Light 1: ON AC: ON\
                                        Sub Corridor 1 Light 1: OFF AC: OFF\
                                        Sub Corridor 2 Light 2: ON AC: ON\
                                                    Floor 2\
                                        Main Corridor 1 Light 1: ON AC: ON\
                                        Sub Corridor 1 Light 1: OFF AC: ON\
                                        Sub Corridor 2 Light 2: OFF AC: ON"

    default_equipment_sub_corridor = "Light 1: OFF AC: ON"

    sub_corridor_default = f"Sub Corridor 1 {default_equipment_sub_corridor}"

    sub_corridor_light_on = "Sub Corridor 1 Light 1: ON AC: ON"

    ac_on = "AC: ON"

    light_on = "Light 2: ON"


