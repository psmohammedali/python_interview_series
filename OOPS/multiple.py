class grandfather:
    def __init__(self):
        print("Grand Father is Printed")
        self.name = "hussain"



class grandmother:
    def __init__(self):
        print("Grand Mother is Printed")
        self.name = "athama"



class father(grandfather, grandmother):
    def __init__(self):
        super().__init__()
        super().__init__()
        # self.name = "abdulla"
        print(self.name)


class mother:
    def __init__(self):
        print("Mother is Printed")
        self.name = "mummy"


class child(father, mother):
    def __init__(self):
        super().__init__()
        print("Child is printed")
        print(self.name)


c1 =  father()



