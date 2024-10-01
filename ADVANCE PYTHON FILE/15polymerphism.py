class Horse:
    def walk(self):
        print("Horse Walking - Tabdak Tabdak")

class Duck:
    def walk(self):
        print("Duck Walking - Thapak Thapak")

class Cat:
    def sound(self):
        print("The cat sound - Meow")

def  animalwalk(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'sound'):
        obj.sound()

h= Horse()
animalwalk(h)

d=Duck()
animalwalk(d)

c= Cat()
animalwalk(c) 

