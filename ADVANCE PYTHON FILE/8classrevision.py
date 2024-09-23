#basic class method

class Animal(object):
    x= 5

print(Animal)
print(Animal.x)






#using __init__ constructor without __str__

class Car:
    def __init__(self):
        self.color = "red"
        self.speed = 100
    
a=Car()
print(a.color)
print(a.speed)

#using __init__ constructor with __str__

class CPU:
    def __init__(self):
        self.processor="Intel Core I7"
        self.ssd="512GB"

    def __str__(self):
        return f"Processor: {self.processor} Ram: {self.ssd}"    
    
cp=CPU()

print(cp)


#Class Object Methods



class Computer:
    def __init__(self):
        self.cpu = "Intel"
        self.ram="8GB"

    def show(self):
        print("Cpu:",self.cpu,"Ram:",self.ram)

c=Computer()
c.show()


#The self Parameter
#we can use any keyword insted of self but have to write a parameter args first

class Watch:
    def __init__(myself,name,age):
        myself.name = name
        myself.age=age

    def show(bio):
        print("Name:",bio.name,"Age:",bio.age)

a=Watch("Ashish",26)
a.show()
a.age=40  #update object value
print(a.age)
a.name="Rinku"
print(a.name)
print(f"Name: {a.name} Age: {a.age}")

#delete object

# del a.age
# print(a.age)


class Ani:
    pass



    