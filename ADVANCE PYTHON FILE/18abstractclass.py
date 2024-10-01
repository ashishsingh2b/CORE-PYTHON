from abc import ABC,abstractmethod


class IndianDefence(ABC):
    def __init__(self):
        self.Armyid=101
        self.Navyid=101
        self.Afid=101
        
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47 ")

class Army(IndianDefence):
    def area(self):
        print("Area = Land","ArmyId:",self.Armyid)

class  Navy(IndianDefence):
    def area(self):
        print("Area = Sea","Navy ID:",self.Navyid)

class Airforce(IndianDefence):
    def area(self):
        print("Area = Sky","AfId:",self.Afid)

print()
print("This area Belong to Indian Army")

a= Army()
a.gun()
a.area()
print()
print("This area Belong to Indian Nvay")

n=Navy()
n.gun()
n.area()
print()
print("This area Belong to Indian Airforce")

af= Airforce()
af.gun()
af.area()

