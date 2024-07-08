# #1 using basic function

# def double(x):
#     return x*2

# number= [1,2,3,4,5,6,7,8]
# doublle_number = list(map(double,number))
# print(doublle_number)


# #2 using lambda function

# def doublefourtime(x):
#     return x*4
# number  = [2,4,6,8,10,12,14,16,18,20]
# double_number= list(map(lambda x: x*4,number))
# print(double_number)


def doublenone1(x):
    return x*2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(doublenone1, numbers))
print(doubled_numbers)  # आउटपुट: [1, 2, 3, 4, 5]


