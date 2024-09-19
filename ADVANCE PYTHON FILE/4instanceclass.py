class Mobile:
    def __init__(self):
        self.model="Iphone 14"

    def show(self):
        print("Ipone Model:",self.model)
    
    def newstock(self,n):
        self.newmodel=n
        print("New Model",self.newmodel)



phone=Mobile()
phone.show()
newphone=Mobile()
phone.newstock("Ihone 16")

#####Accessor or Getter Method and Mutator or Setter Method in Python (Hindi)######

class Animal:
    def __init__(self):
        self.name= "Dog"

    def set_name(self):
        self.name = "german"
        

AnimalName=Animal()
print(AnimalName.name)

AnimalName.set_name()
print(AnimalName.name)
