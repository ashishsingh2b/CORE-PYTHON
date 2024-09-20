# class Student:
#     def __init__(self,n,r):
#         self.name=n
#         self.roll=r

#     def show(self):
#         print("Name:",self.name)
#         print("Roll:",self.roll)


# class User:
#     @staticmethod
#     def showuser(s):
#         print("User Name",s.name)
#         print("User Roll",s.roll)
#         s.show()
# stu= Student("Rahul",101)

# User.showuser(stu)

# new

# class Persion:
#     def __init__(self,name):
#         self.name =name

#     def show(self):
#         print("Persion name:",self.name)

# class Address:
#     def __init__(self,street,city):
#         self.street=street
#         self.city=city

#     @staticmethod
#     def details(s):
#         print("Street:",s.street)
#         print("City:",s.city)
#         print("City:",s.persion)

# per=Persion("Ashish")

# Address.details(per)


class Person:  # Fixed spelling from 'Persion' to 'Person'
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Person name:", self.name)

class Address:
    def __init__(self, street, city,person=None):
        self.street = street
        self.city = city
        self.person=person

    @staticmethod
    def details(address):  # Changed parameter name to 'address'
        print("Street:", address.street)
        print("City:", address.city)
        if address.person:

                      print("Persion:", address.person.name)
        

# Create an instance of Person
per = Person("Ashish")

# Create an instance of Address
addr = Address("123 Main St", "Cityville",per)

# Display address details
Address.details(addr)




        