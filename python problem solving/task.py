#Task 1 

# :-count the each string 
# name= "my name is Mann"

# eg. m=3, y=1, n=3

# name = "my name is Mann"

# m = name.count("m")
# y = name.count("y")
# n = name.count("n")

# print("m={},y={},n={}".format(m,y,n))


#Task 2
# dict1 = {"id":1, "name":"mann"}
# dict2 = {"id2":3, "name2":"Rohit"}
# dict3 = {"id3":5, "name3":"Virat"}


# merge all:-
# {'id': 1, 'name': 'mann', 'id2': 3, 'name2': 'Rohit', 'id3': 5, 'name3': 'Virat'}

# dict1 = {'id': 1, 'name': 'mann'}
# dict2 = {'id2': 3, 'name2': 'Rohit'}
# dict3 = {'id3': 5, 'name3': 'Virat'}

# merged_dict = {**dict1, **dict2, **dict3}
# print(merged_dict)

#Task 3
# dict1 = {"id":1, "name":"mann"}
# dict2 = {"id":3, "name":"Rohit"}
# dict3 = {"id":5, "name":"Virat"}
# merge all
# Result = {'id': 1, 'name': 'mann'} {'id': 3, 'name': 'Rohit'} {'id': 5, 'name': 'Virat'}

# dict1 = {"id":1, "name":"mann"}
# dict2 = {"id":3, "name":"Rohit"}
# dict3 = {"id":5, "name":"Virat"}

# merger_cell = dict1,dict2,dict3
# print(merger_cell)


# arrange alphabatic manner 
# response ={'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorteddict = dict(sorted(myDict.items()))
print(sorteddict)
