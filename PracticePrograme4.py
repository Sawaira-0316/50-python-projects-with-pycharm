#num=int(input("enter a number"))
#print('last digit of number',num%10)

num = int(input("enter a number"))
Id=num%10
if Id%3==0:
    print("number last is divisible  by 3")
else:
    print("number is  not divisble by 3")