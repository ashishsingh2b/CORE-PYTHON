a  = [25,26,28,40,48,'Ashish Singh']

print(a,id(a))
print(a[1])
a[2] = 100
print(a,id(a))
ab = []
print(ab)


for element in a:
    print(element)


print(len(a))
n = len(a)

for i in range(n):
    print("index:",i,a[i])