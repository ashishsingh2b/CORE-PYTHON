# num =8
# num_sqrt= num ** 0.5

# print(num_sqrt)

# num = int(input("Enter the number:"))

# root= num * num
# # root= num ** 0.5
# print(root)  # Output: 3.0
# import math
# num = int(input("Enter the number:"))

# root = math.sqrt(num)
# print(root)  # Output: 3.0


import cmath

num = 1+2j

num_root=cmath.sqrt(num)
print(num_root)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_root.real,num_root.imag))

