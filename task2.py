 python task 2 on lists.
  
1.
ls=[10,20,[30,40,[50,60],80],90,100]
h=ls[2][2]
h.append(70)
print(ls) 
              output:ls=[10,20,[30,40,[50,60],80],90,100]    

2.
ls=[1,2,[3,4,5,6],9]
h=ls[2]
j=[[7,8]]
ls2=h.extend(j)
print(ls)
             output:ls=[1,2[3,4,5,6,[7,8]],9] 
  
  some in_built functions
  1.remove()- This function helps to remove specified object at its first occurance from the list.
>>> ls=[1,2,3,4,5,5,6.6,"anaconda","python"]
>>> ls.remove(3)
>>> ls
[1, 2, 4, 5, 5, 6.6, 'anaconda', 'python']
>>> ls.remove("python")
>>> ls
[1, 2, 4, 5, 5, 6.6, 'anaconda']    
    
  2.count()- This function helps to count the specified variable, that has occured in the list.  
>>> ls=[1,2,2,2,2,3,3,6,7,"data","variable"]
>>> ls.count(2)
4
>>> ls.count("data")
1

  3.clear()- This function clears the list.
>>> ls=[1,2,2,2,2,3,3,6,7,"data","variable"]
>>> ls.clear()
>>> ls
[]
>>> len(ls)
0

  4.sort()- This function sorts the elements of the list in ascending or descending order.
>>> ls=[34,89,3,6,0.7,7.2,19]
>>> ls.sort()
>>> ls
[0.7, 3, 6, 7.2, 19, 34, 89]
>>> ls.sort(reverse=true)
>>> ls
[89, 34, 19, 7.2, 6, 3, 0.7]

 5. reverse()- This function reverses the elements of the list ,right to left of the list.
>>> ls
[89, 34, 19, 7.2, 6, 3, 0.7]
>>> ls.reverse()
>>> ls
[0.7, 3, 6, 7.2, 19, 34, 89]
>>> ls=[-78,-0.67,4,67,23,-12]
>>> ls.reverse()
>>> ls
[-12, 23, 67, 4, -0.67, -78]
