class Father:
    def __init__(self,m):
        self.monery= m
        print("Father class contructor called")

    def show(self):
        print("Parent Class Money ",self.monery)

class Son(Father):
    def disp(self):
        print("Child Class Money ",self.monery+99999)

s= Son(100000)
s.show()
s.disp()