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

# name= "my name is mann"

# m = name.count("m")
# y = name.count("y")
# n = name.count("n")

# #print(f"m={m},y={y},n={n}")
# print("m={},y={},n={}".format(m,y,n))

# a = int(input("Enter a number:"))
# if a==1:
#     print("this is not a prime number",a)

# if a>3:
#     if a%2==0:
#         print("This is not a prime number",a)
#     else:
#         print("This is a prime number",a)

a=int(input("Enter a number:"))
if a==1:
    print("this is not a prime number")


if a>1:
    
     for i in range(2,a):
       if i%a==0:
         print("This is not a prine num")
       else:
         print("This is a prime number")



 