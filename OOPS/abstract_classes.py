from abc import ABC, abstractmethod


class automobile():
    def __init__(self):
        self.wheels = "wheels"

    def start(self):
        print("Automobile start")


class car(automobile):
    def __init__(self, wheels):
        super().__init__()
        # self.wheels = wheels

    def start(self):
        print("Car start")
        print(self.wheels)


c = car(4)
c.start()
