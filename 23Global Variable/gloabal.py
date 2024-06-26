
#local variable
def myfun():
    i=15
    a=i+15
    print(a)

    print("My local valiable is:", i)

myfun()


#global variable
x=20
def mynewfun():
    y = x + 20
    print(y)
    
    print("My GLobal Variable is :", x )

mynewfun()

#global variable similar name assign

x= 20
def mydub():
    x=10
    x=x+20
    print("dublicate:",x)

mydub()

#global keyword

ab= 15

def mynum():
  #  ab = 16
    global ab

    ab= ab+20
    print(ab)

    print()

mynum()

# num fun

i = 0
def num():
    global i
    while i<5:
        i+=1    
        print(i)

num()
    

