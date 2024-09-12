# a = {"bio":{"Name":"Ashish","Roll":101,"City":"Surat"},
#      "bio2":{"Name":"Gautam","Roll":102,"City":"Navsari"}}

# print(a)
# print(a['bio'])
# print(a['bio2'])
# print(a['bio']['Name'])
# print(a['bio']['Roll'])
# print(a['bio']['City'])
# print(a['bio2']['Name'])
# print(a['bio2']['Roll'])
# print(a['bio2']['City'])

a = {"bio":{"Name":"Ashish","Roll":101,"City":"Surat"},
     "bio2":{"Name":"Gautam","Roll":102,"City":"Navsari"}}

for i in a:

    for j in a[i]:
       # print(j)
        print(j,"=",a[i][j])
