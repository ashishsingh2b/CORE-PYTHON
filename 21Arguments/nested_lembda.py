add  = lambda x=20 : (lambda y:x+y)
a = add()
print(a)
print(a(20))

#lambda function in another passing
def add (a):
    print(a(8))

add(lambda x:x)

#Returning Lambda Function from a Function in Python

def add():
    y=10
    return (lambda x:y+x)
a=add()
print(a(20))


