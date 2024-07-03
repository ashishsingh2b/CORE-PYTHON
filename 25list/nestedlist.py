b= [20,15,18,17,[15,18,17]]
a = [15,5,15,45,b]

print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4][0])
print(a[4][1])
print(a[4][2])
print(a[4][3])

print(b)

b[4][0] = 100

print(b)