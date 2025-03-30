class vehicle:
    def __init__(self, object_color, obj_speed):
        self.color = object_color
        self.max_speed = obj_speed

    def print(self):
        print("Vehicle Object: ", self.color, self.max_speed)


class bike:
    pass


class car(vehicle):
    def __init__(self, no_of_doors, no_of_gears, object_color, obj_speed):
        # super().__init__(object_color, obj_speed)
        super().__init__(object_color, obj_speed)
        self.doors = no_of_doors
        self.gears = no_of_gears

    # def print(self):
    #     print("This is car object")

    def second_print(self): 
        # super().print()
        self.print()

honda = car(4, 5, "white", 20)
honda.second_print()
