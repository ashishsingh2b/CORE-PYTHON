a = {"Name":"Ashish","Lname":"Singh","Bio":{"roll":101,"Add":"Surat","Age":26}}

for i in a:
    print(i)


for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k, "=",a[i][k])
            
    else:
        print(i, "=",a[i])