 task on tuple
 To add and remove elements in tuple

t=(1,2,3,5,7,9,4,6)
ls=list(t)
ls.append(8)
print(ls)
 #output: [1, 2, 3, 5, 7, 9, 4, 6, 8]
ls.sort()
ls.remove(8)
print(ls)
#output: [1, 2, 3, 4, 5, 6, 7, 9]
ts=tuple(ls)
print(ts)
#output: (1, 2, 3, 4, 5, 6, 7, 9)


task on sets
1.Difference()
 The difference between two sets results in a third set with the element from the first,that are not present on the second. This operation is not commutative.
  
s={1,2,3,4}
a={3,4,5,6}
print(s.difference(a))
#output: {1, 2}

print(a.difference(s))
#output: {5, 6}

2.Symmetric difference()
  The symmetric difference between two sets results in a third set with the elements,from both sets, that are not present on the other.
  
s={"rahul","kavita","vinod","swaroop","kiran"}
a={"ram","vinod","satish","prajwal","swaroop"}
print(s.symmetric_difference(a))
#output: {'kiran', 'kavita', 'ram', 'satish', 'prajwal', 'rahul'}

print(a.symmetric_difference(s))
#output: {'kiran', 'ram', 'kavita', 'rahul', 'satish', 'prajwal'} 
