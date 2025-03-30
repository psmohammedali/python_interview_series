class student:
    def __init__(self,name, id):
        self.name = name
        name = name + "abc"
        self.__id = id
        print(name)
    def object_method(self):
        print("This is object method")

    @staticmethod
    def class_method():
        print("This is class method")


s1 = student("Ali",1)
s1.class_method()
s1.object_method()

