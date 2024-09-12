mydict ={}

n= int(input("Enter How many dict Yoy want: "))

for i in range(n):
    k = input("Enter The Key :")
    v= input("Enter The Key value:")
    mydict.update({k:v})
    print(mydict)
