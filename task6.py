task on looping concept

1.printing numbers from 10 to 1

c=10
while(c>0):
    print(c)
    c-=1

output:
10
9
8
7
6
5
4
3
2
1

2a.
for loop which uses lists.
l=[1,2,3,4,5,9,5,6,6,7,9]
l1=[]
for i in l:
    if(i not in l1):
        l1.append(i)
    continue
print("The list after removing duplicate {} from original list {}".format(l1,l))
l1.sort()
print(l1)

output:
The list after removing duplicate [1, 2, 3, 4, 5, 9, 6, 7] from original list [1, 2, 3, 4, 5, 9, 5, 6, 6, 7, 9]
[1, 2, 3, 4, 5, 6, 7, 9]

2b.
for loop which uses tuple.
t=("a","1","b","5","c","9")
d,e=0,0
for i in t:
    if(i.isalpha()):
        d+=1
    elif(i.isdigit()):
        e+=1
    else:
        pass
print("The number of alphabets are {} and number of digits are {} ".format(d,e))

output:
The number of alphabets are 3 and number of digits are 3

2c.
for loop which uses dictionary.
* enter values() in numbers only
s=0
d={"a":1,"b":2,"c":3,"d":4}
for a,b in d.items():
       s=b+s
print("The sum of values {} are {}".format(list(d.values()),s))

output:
The sum of values [1, 2, 3, 4] are 10



