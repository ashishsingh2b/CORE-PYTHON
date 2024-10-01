class Add:
    def result(self,x,y):
        print("Addition:",x+y)
    
class Multi(Add):
    def result(self,a,b):
        super().result(10,10)
        print("Addition:",a*b)
    
m=Multi()
print(m.result(10,10))