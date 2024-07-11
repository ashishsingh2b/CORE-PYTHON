#accessig tuple using for loop

a= (15,20,25,"Ashish Singh")


#without index
for element in a:
    print(element)

#with index

n = len(a)    

for i in range(n):
    print(a[i])
    print("the index is:",i,a[i])
