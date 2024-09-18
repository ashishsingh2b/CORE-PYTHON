#call the constructor

class Mobile:
    def __init__(self):
        print("constrocture is called")

samsung = Mobile()

#without argument constructor

class Samsumg:
    def __init__(self):
        self.model = "Samsung Z Fold"
        self.price = 1000
        print("Model:",self.model,"Price:",self.price)

Samsumg()


class Apple:
    def __init__(self,m):
        self.model = m
        print("model:",self.model)

Apple("Iphone16")


#default variable value

class Iphone:
    def __init__(self,m,y=2024):
        self.model = m
        self.year =y

    def show_details(self):
        print("Model:",self.model,"Year:",self.year)
    
bio = Iphone("Iphone 16")
bio.show_details()

newbio=Iphone("Iphone 17 Pro",2025)
newbio.show_details()
