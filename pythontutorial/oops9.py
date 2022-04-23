# multilevel inheritance

class Dad:
    basketball = 6


class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"I can dance {self.dance} number of times."


class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Hell Yeah I can dance {self.dance} number of times."


yama = Dad()
dharma = Son()
raja = Grandson()

print(raja.isdance())
print(raja.basketball)