# class School(object):
#     def student(self):
#         print("Ram is  a student of Sun school")

# sch = School()
# sch.student()

# class  Aschool(object):
#     def fees(self):
#         print("Ram's Fee is pending")

# stfees=Aschool()
# stfees.fees()

# class Myclass(object):
#     def absent(self):
#         print("Dear Parents Ram Is absent Today")

# Myclass().absent()
# abs=Myclass()
# abs.absent()


# class Collage(object):
#     def start(self):
#         print("Collage Starts at 9:00 AM")

# time=Collage()
# time.start()


#static
class Mobile:
    def __init__(self):
        self.model = "Iphone 14"
        self.price = 99999
    
    def  display(self):
        self.owner= "Ashish"
        print("Owner:",self.owner,"Model:",self.model,"Price:",self.price)

iphone=Mobile()
iphone.display()
print(id(iphone))


#Dynamic

# class Car:
#     def __init__(self,c,d):
#         self.model = c
#         self.color = d

#     def  display(self,o):
#         self.owner = o
#         print("Owner:",self.owner,"Model:",self.model,"Color:",self.color)

# details=Car("Farraritg","Red")
# details.display("Ashish")
# print(id(details))




class Computer:
    def __init__(self):
        self.opsy = "Windows"
        
    def show(self):
        self.company = "Microsoft"
        self.price = "25999"
        print("Company:",self.company,"Price:",self.price,"OPerating:",self.opsy)

com= Computer()
com.show()
print(id(com))


class Computer:
    def __init__(self,c):
        self.opsy = c
        
    def show(self,a,b):
        self.company =a
        self.price =b
        print("Company:",self.company,"Price:",self.price,"OPerating:",self.opsy)

com= Computer("Windows")
com.show("Microsoft",25999)
print(id(com))

com= Computer("Linux")
com.show("Linux",25999)
print(id(com))