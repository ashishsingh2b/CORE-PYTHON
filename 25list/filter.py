# Example Usage:
# 1.Using a Regular Function:

def is_positive(x):
    return x>0

num = [-2,-1,0,1,2]

positive_number =list(filter(is_positive,num))
print(positive_number)


# 2.1.Using a Regular Function:


def is_negativenumber(x):
    return x<0
num1 = [-2,-1,0,1,2]
negative_number= list(filter(is_negativenumber,num1))
print(negative_number)


#3 Using a Lambda Function:

def is_positivenumber(x):
    return x>0
numbers=[-2,-1,0,1,2]
positive_number = list(filter(lambda x:x>0,numbers))
print(positive_number)

#4.Using None as the Function:

def is_positivenumber(x):
    return x>0
numbers=[-2,-1,0,1,2]
positive_number= list(filter(None,numbers))
print("This Is using by None: ",positive_number)
    