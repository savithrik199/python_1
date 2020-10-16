task on conditional statement

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

#output
enter first number  4
enter second number  5
enter z  1
addition of 4 and 5 is 9

enter first number  7
enter second number  9
enter z  2
subtraction of 7 and 9 is -2 

enter first number  -3
enter second number  -5
enter z  3
multiplicati of -3 and  -5 is 15

enter first number  -72
enter second number  9
enter z  4
division of -72 and 9 is -8.0


