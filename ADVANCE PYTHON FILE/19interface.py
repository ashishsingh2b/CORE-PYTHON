#Interface class is abstract class without concreate class only having  abstract method

from abc import ABC,abstractmethod

class Defence(ABC):
    @abstractmethod
    def defend(self):
        pass

class  Soldier(Defence):
    def defend(self):
        print("Soldier is defending")

s=Soldier()
s.defend()