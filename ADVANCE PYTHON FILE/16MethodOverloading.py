
#basic format when args=value
# class Myclass:
#     def sum(self,a,b,c):
#         s=a+b+c
#         return s
    
# su=Myclass()
# print(su.sum(10,12,15))


#basic format when args!=value
class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
              s=a+b+c
        elif a!=None and b!=None:
              s=a*b
        else:
             s="Provide at least two number"
              
        return s
    
su=Myclass()
print(su.sum(10))