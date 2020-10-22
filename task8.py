task on list comprehensions and scope

1.
l={3,15,20,30,60}
l1=[]
l1=[i  for i in l  if i%3==0 if i%5==0]
print(l1)

output-[15,30,60]

2.
names=["ad","cd","ef"]
food=["dr","jk","kl"]
l1=[i+j for i,j in zip(names,food) if i!="ad"  ]
print(l1)

output-['cdjk', 'efkl']


3.
ms="p"

def gr():
    ms="l"


print(ms)

output- p
