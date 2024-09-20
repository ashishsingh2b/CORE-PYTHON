class Mobile:
    @classmethod                 #class method decorator
    def show_model(cls):         #class method
        print("Samsung")

sam=Mobile()
Mobile.show_model()             #calling class method


class Animal:
    wild = "Yes"
    @classmethod               #class decorator
    def show_animal(cls):      #class method
        print("Lion",cls.wild)

wildanimal= Animal()
Animal.show_animal()            #calling class method


class  Doctor:
    heartspecialist = "Yes"
    @classmethod
    def  show_doctor(cls,d):
        cls.doctor = d
        print("decision:",cls.heartspecialist,"specific_doctor:",cls.doctor)

doctordetails = Doctor()
Doctor.show_doctor("Cergen")


#class static method

class Myself:
    @staticmethod
    def show_myself():
        print("My name is Ashish")

iam=Myself()
Myself.show_myself()            #calling static method

class Dog:
    @staticmethod
    def show_dog(b,n):
        bread = b
        name = n
        print("Dog_Bread:",bread,"Dog_name:",name)

dogy= Dog()
Dog.show_dog("Gernan","Rockey")



#when to use

class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposite(self,amount):
        self.amount =  amount
        print("Deposite_balance:",self.amount)

    def get_balance(self):
        return self.balance
ac=BankAccount()
ac.deposite(100)
print(ac.get_balance())            #calling instance method

    
        
