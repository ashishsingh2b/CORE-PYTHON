mydict = {"Name":"Ashish","roll":101,"Sr":1}
print(mydict)
print(type(mydict))

#update

mydict['Name']="Bittu"
print(mydict)
print("Sr :",mydict["Sr"])
print("Name :",mydict["Name"])
print("Roll :",mydict["roll"])

#added

mydict["Age"]= 26
print(mydict)

#delete

del mydict['Sr']
print(mydict)
