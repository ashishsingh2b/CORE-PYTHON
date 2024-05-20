# :-count the each string 
# name= "my name is Mann"

# eg. m=3, y=1, n=3

# pattern 1
# test_str = "my name is Mann"
# all_freq = {}

# for i in test_str:
# 	if i in all_freq:
# 		all_freq[i] += 1
# 	else:
# 		all_freq[i] = 1


# print("Count of all characters=\n "
# 	+ str(all_freq))

name= "my name is mann"

m = name.count("m")
y = name.count("y")
n = name.count("n")

#print(f"m={m},y={y},n={n}")
print("m={},y={},n={}".format(m,y,n))
