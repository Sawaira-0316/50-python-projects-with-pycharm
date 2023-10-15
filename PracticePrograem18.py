nd=int(input("enter Total number of working days"))
na=int(input("ente the number days of absent"))
per=(nd-na)/nd*100
print("Your attandence is ",per)
if per>75:
    print("you are eligibale for exams" )
else:
    print("you are not eligible")