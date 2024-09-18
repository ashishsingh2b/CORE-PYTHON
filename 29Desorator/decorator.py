def myself():
    print("Hii My name is Ashish SIngh")
    print("My father name is Shree Pravin Singh")

# myself()


def  my_family(fun):
    def inner():
        print("My family is very good")
        fun()
        print("My family Hvae A better Future")
    return inner

def num():
    print("I am Ashish Singh")
    print("I am Also  a good programmer")

result_fun=my_family(num)
result_fun()  # Output: My family is very good I am Ashish Singh I am Also


def decor(number):
    def inner():
        a=number()
        add=a+10
        return add
    return inner

# def number():
#     return 10

# number=decor(number)
# print(number())

@decor
def number():
    return 10
print(number())

#task 1 change the retun 10 to retun 50

def decor(sum):
    def inner():
        a=sum()
        newsum= a+45
        return newsum
    return inner

#change the code to retun the value 100

def decor1(sum):
    def inner():
        b=sum()
        newsumm= b + 45
        return newsumm
    return inner

def sum():
    return 10

sum = decor1(decor(sum))
print(sum())
