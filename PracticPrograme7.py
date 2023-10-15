yr=int(input("Enter a year"))
if yr%100==0:
    if yr%400==0:
        print("this is leap year")
    else:
        print("this is not leap year")
else:
    if yr%4==0:
        print("this is leap year")
    else:
        print("this  is not leap year")