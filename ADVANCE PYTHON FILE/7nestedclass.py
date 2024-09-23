class Army:
    def __init__(self):
        self.name= "Capton A.K. Singh"
        self.gn= self.Gun

    def show(self):
        print(f"Name: {self.name}")

    
    class  Gun:
        def __init__(self):
            self.name= "AK-47"
            self.caliber= "7.62mm"
            self.made=  "Russia"
        def disp(self):
            print(f"Name: {self.name}")
            print(f"Caliber: {self.caliber}")   
            print(f"Made: {self.made}") 

a= Army()
a.show()

g=Army().Gun()

g.disp()


