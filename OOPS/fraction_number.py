class fraction:
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    def add(self, frac_obj):
        self.num = self.num * frac_obj.deno + self.deno * frac_obj.num
        self.deno = self.deno * frac_obj.deno
        self.__simplification()

    def mul(self, frac_obj):
        self.num = self.num * frac_obj.num
        self.deno = self.deno * frac_obj.deno
        self.__simplification()

    def __simplification(self):
        # finding highest common divisor
        num1 = min(self.num, self.deno)
        num2 = max(self.num, self.deno)
        rem = num2 % num1

        while rem != 0:
            print(num2, num1)
            num2 = num1
            num1 = rem
            rem = num2 % num1
        gcd = num1

        self.num = self.num // gcd
        self.deno = self.deno // gcd

    def print_fraction(self):
        self.__simplification()
        print(self.num, "/", self.deno)


frac1 = fraction(20, 30)
frac2 = fraction(30, 20)
frac1.print_fraction()
frac1.add(frac2)
frac1.print_fraction()
