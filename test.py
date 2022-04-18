class Figury:
    def __init__(self,a,h=0):
        self.a = a
        self.h = h

    def pole_pow(self,a,h):
        return self

class Kwadrat(Figury):
    def pole_pow(self):
        return self.a*self.a

class Trojkat(Figury):
    def pole_pow(self):
        return self.a*self.h/2

kwadrat = Kwadrat(5)
trojkat = Trojkat(2,5)

print(kwadrat.pole_pow())
print(trojkat.pole_pow())

'''The end of the program - AG'''