class Father(object):
    def __init__(self):
        super().__init__()
        print("Father Constructor is called")

    def showF(self):
        print("Father is called")

class  Mother(object):
    def __init__(self):
        super().__init__()
        print("Mother Constructor is called")

    def showM(self):
        print("Mother is called")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Son class constructor is called")
    def showS(self):
        print("Son is called")

s=Son()
s.showF()
s.showM()
s.showS()