class my_class(object):
    def print_time(self):
        print(self.__init__())
        print(super().__init__())

    def __str__(self):
        print()


c1 = my_class()
c1.print_time()
