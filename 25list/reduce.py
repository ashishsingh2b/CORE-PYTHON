from functools import reduce
#बिना इनिशिएलाइजर:
number =[1,2,3,4,5]
sub= reduce(lambda x,y:x+y,number)
print(sub)


#इनिशिएलाइजर के साथ:

number1= [1,2,3,4,5]
product=reduce(lambda x,y:x+y,number,1)
print(product)