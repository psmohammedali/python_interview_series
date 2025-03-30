class father:
    def __init__(self):
        self.name = "abdulla"

    def print(self):
        return self.name

class son(father):
    def __init__(self):

        super().__init__()
        self.name = "ali"

    def print(self):
        print(self.name)
        print(super().pri)

s = son()
s.print()



