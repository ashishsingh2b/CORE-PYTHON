a = [25,30,35,40,45]
b=a

print(a)
print(b)
print(id(a))
print(id(b))
a= a[0:2]
b= b[0:3]
print(a)
print(b)
print(id(a))
print(id(b))