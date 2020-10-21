task on functions

1.
def no(n1,n2):
    x=n1
    y=n2
    return x,y

num1=int(input("enter first number"))
num2=int(input("enter second number"))
a,b=no(num1,num2)
print("first and second number is {} and {}".format(a,b))

output:
enter first number 23
enter second number 12
first and second number is 23 and 12


2.
''' press 1 for addition
 press 2 for subtraction
 press 3 for multiplication
 press 4 for division'''
def op(i):
      x=int(input("enter first number"))
      y=int(input("enter second number"))
      if(i==1):
          z=x+y
          print("sum of {} and {} is {}".format(x, y, z))
      elif(i==2):
          z=x-y
          print(" difference of {} and {} is {}".format(x, y, z))
      elif(i==3):
          z=x*y
          print("product of {} and {} is {}".format(x, y, z))
      elif(i==4):
          z=x/y
          print("division of {} and {} is {}".format(x, y, z))
      else:
          print("invalid i")

j=int(input("enter valid i"))
op(j)

output:
enter valid i 3
enter first number 90
enter second number 78
product of 90 and 78 is 7020

3.
def sum(x,y):
    z=x+y
    return z

def diff(x,y):
    z=x-y
    return z

def pod(x,y):
    z=x*y
    return z

def div(x,y):
    z=x/y
    return z

a=int(input("enter first number"))
b=int(input("enter second number"))
i=sum(a,b)
j=diff(a,b)
k=pod(a,b)
l=div(a,b)
print("sum of {} and {} is {}".format(a,b,i))
print("difference of {} and {} is {}".format(a,b,j))
print("product of {} and {} is {}".format(a,b,k))
print("division of {} and {} is {}".format(a,b,l))

output:
enter first number 45
enter second number 90
sum of 45 and 90 is 135
difference of 45 and 90 is -45
product of 45 and 90 is 4050
division of 45 and 90 is 0.5








