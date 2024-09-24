#Inheritance topic

#------------Single Inheritance---------------#

class Father:
    money = 1000

    def show(self):
        print("Print Class Instance Ineritance")

    @classmethod
    def showmoney(cls):
        print("Parents Class Method ",cls.money)

    @staticmethod
    def  start():
        amount = 90000
        print("Static method",amount)

class Son(Father):
    def disp(self):
        print("Child Class Method")

a=Son()
a.disp()
a.show()
a.showmoney()
a.start()
print("Space between")
b=Father()

b.show()
b.showmoney()
b.start()



