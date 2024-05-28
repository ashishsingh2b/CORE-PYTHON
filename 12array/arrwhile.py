from array import *
array_list = array('i',[12,15,18,17,16,120,157,500,1500])
array_list.append(127845)
n=len(array_list)
i=0
while i<n:
    print(array_list[i])
    i+=1

# array_list1 = array('i',[12,15,18,17,16,120,157,500,1500])
# array_list2 = array('i',[12,15,18,17,16,120,157,500,1500])
# array_list1.extend(array_list2)
# print(array_list1)