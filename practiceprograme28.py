num=int(input("enter the number"))
s=0
while(num):
    r=num%10
    s=s+r
    num=num//10
    print("sum of digits is",s)