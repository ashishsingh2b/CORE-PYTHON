class Father(object):
    def __init__(self):
        
        print("Father Class Constructor called")
    def show(self):
        print("Father class Instance")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor called")
    def showS(self):
        print("Son Class Instance")

class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("Grandson Class Constructor called")
    def showG(self):
        print("GrandSon Class Instance")

g=GrandSon()
g.showG() # Output: Grandson class Instance
g.showS() # Output: Son class Instance
g.show()  # Output: Father class Instance