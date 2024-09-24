class Father:
    def __init__(self,m):
        self.money=m
        print("Parents Constructor Is Called")
    
    def show(self):
        print("Parets Instance Method",self.money)

class Son(Father):
    def __init__(self,r):
        super().__init__(r)
        print("Son ConsTructor is Called")
    def disp(self):
        print("Son Instance Method",self.money)

s=Son("One Lack")
s.show()
s.disp()

