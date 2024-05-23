year = int(input("Enter Year:"))

if (year%400==0) and (year%100==0):
    print(year,"This is a leap year")
elif (year%4==0) and (year%100!=0):
    print(year,"this is a leap year")
else:   
    print(year,"This is not a leap year")