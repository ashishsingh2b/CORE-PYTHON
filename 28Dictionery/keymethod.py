mydict = {"Hindi":15,"English":20,"Math":35,"Science":45,"FName":"Ashish","LName":"Singh"}

all_keys=mydict.keys()
print(all_keys)
print(type(all_keys))

for k in all_keys:
    print(k)

    
print()

all_value = mydict.values()
print(all_value)
print(type(all_value))

for v in all_value:
    print(v)