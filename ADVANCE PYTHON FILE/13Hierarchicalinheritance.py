class Father(object):
    def __init__(self):
        super().__init__()
        print("Father Constructor Called")

    def showF(self):
        print("Father Is Called")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Constructor Called")

    def showS(self):
        print("Son Is Called")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter Constructor Called")

    def showD(self):
        print("Daughter Is Called")

print("Father Started")

s=Son()
s.showF()
s.showS()

print("Daughter Started")

d=Daughter()
d.showF()
d.showD()
    