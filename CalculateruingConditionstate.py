print('''
 + ADD
 _ SUBTRACT
 * mULTIPLICATION
 / dIVISION
''')
num1=int(input("Enter the first number"))
num2=int(input("Eter the second numbe"))
op=input("enterthe op...")
if op=="+":
    print(num1+num2)
elif op=="_":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid opeator")