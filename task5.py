x=int(input("enter first number  "))
y=int(input("enter second number  "))
'''enter z as per
    z=1 (addition)
    z=2 (subtraction)
    z=3 (multiplication)
    z=4 (division)'''
z=int(input("enter z  "))
if(z==1):
    sol=x+y
    print("addition of {} and {} is {}".format(x,y,sol))
elif(z==2):
    sol=x-y
    print("subtraction of {} and {} is {} ".format(x,y,sol))
elif(z==3):
    sol=x*y
    print("multiplicati of {} and  {} is {}".format(x,y,sol))
elif(z==4):
    sol=x/y
    print("division of {} and {} is {}".format(x,y,sol))
else:
    print("invalid z")



