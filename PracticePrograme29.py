num=int(input("enter the first number"))
f=0
if num==1 or num==0:
    f=1
for i in range(2,num):
    if num%i==0:
        f=1
if f==1:
    print("the number is prime")
else:
    print("the number is not prime")
