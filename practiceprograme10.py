num1=(input("enter a number"))
i=len(num1)
if i !=3:
    print("entr three digits")
else:
    print("middel digitis" ,(int(num1)%100//10))