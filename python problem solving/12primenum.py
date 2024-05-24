num = int(input("Enter a number"))

if num==1:
    print("this is not a prime number")
if num>1:
    for i in range(2,num):
        if num % i ==0:
            print("This is not a prime number")
        else:
            print ("this is a prime number")

# num = int(input("Enter a Num:"))

# if num==1 or num%2==0:
#     print("This is not a prime number")
# else:
#     print("This is a Prime number")
