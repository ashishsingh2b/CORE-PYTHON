a = ((15,25,30),(20,54,56))
n= len(a)

for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])



for r in a:
    for c in r:
       print(c)
    print()

