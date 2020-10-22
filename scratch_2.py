#l=[3,15,20,30,60]
#l1=[]
'''for i in l:
    if i not in l1:
        l1.append(i)
    pass
print(l1)'''

#l1=[i  for i in l  if i%3==0 if i%5==0]
#print(l1)

#output-[15,30,60]

'''names=["ad","cd","ef"]
food=["dr","jk","kl"]
l1=[i+j for i,j in zip(names,food) if i!="ad"  ]
print(l1)'''

#output-['cdjk', 'efkl']

ms="p"

def gr():
    ms="l"


print(ms)

output- p