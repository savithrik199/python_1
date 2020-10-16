# task on tuple
# To add and remove elements in tuple

t=(1,2,3,5,7,9,4,6)
ls=list(t)
ls.append(8)
print(ls)
ls.sort()
ls.remove(8)
print(ls)
ts=tuple(ls)
print(ts)



