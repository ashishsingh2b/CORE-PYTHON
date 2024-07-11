def show(t):
    print(t)
    for i in t:
        print(i)
    return t


tuple = (15,20,25,30)
show(tuple)
new_tup = show(tuple)
print(new_tup)
print(type(new_tup))