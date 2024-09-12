mydict = {"Hindi":15,"English":20,"Math":35,"Science":45,"FName":"Ashish","LName":"Singh"}


removed_dict = mydict.pop("Hindi")
print(mydict)
print(removed_dict)


mydict1 = {"Hindi":15,"English":20,"Math":35,"Science":45,"FName":"Ashish","LName":"Singh"}

removed_dict1 = mydict1.popitem()
print("Main Dict",mydict1)
print("Removed Dict",removed_dict1)


return_value = mydict1.setdefault("Englishs","Not Found please Try what we have")
print("Return Value",return_value)

