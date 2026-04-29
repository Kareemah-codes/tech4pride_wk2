#Input => year (int)
#Ouput => number of days of month

year = int(input("Enter your year "))

if year % 100 == 0:
    if year % 400 == 0:
        print(29) #It is a leap year
    else:
        print(28)
elif year % 4==0:
    print(29)

else:
    print(28)
    