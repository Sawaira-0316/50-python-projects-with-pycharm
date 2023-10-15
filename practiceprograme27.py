num=int(input("enter the first numbre"))
p=1
while(num):
    r=num%10
    p=p*num
    num=num//10
    print("prodects of digits is",p)