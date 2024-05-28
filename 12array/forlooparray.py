from array import*
array_list = array('i',[])
n=int(input("Enter The Number of Element: "))

for i in range(n):
    array_list.append(int(input("Enter The number of element")))

for i in range(len(array_list)):
    print(array_list[i])