'''Zip() function
The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

Syntax :
zip(*iterators)'''

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

'''for i,j,k in zip(name,y,z):
    if(i=="Nikhil"):
        continue
    print(f" Name is {i} , roll no is {j} ,marks is {k}")

 The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60), ('Astha', 2, 70)]
 Name is Manjeet , roll no is 4 ,marks is 40
 Name is Shambhavi , roll no is 3 ,marks is 60
 Name is Astha , roll no is 2 ,marks is 70'''

#Enemurate()

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
#This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

#synax= enumerate(iterable, start=0)

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

#[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
#[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)


# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(f"{count}, {ele}")

'''Output:

(0, 'eat')
(1, 'sleep')
(2, 'repeat')

100 eat
101 sleep
102 repeat'''

from functools import reduce

lst=[1,2,3,4,5]

print(reduce(lambda a,d:a+d ,lst))

print(reduce( lambda a,c:a*c ,lst))