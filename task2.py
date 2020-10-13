ls=[10,20,[30,40,[50,60],80],90,100]
h=ls[2][2]
h.append(70)
print(ls)

ls=[1,2,[3,4,5,6],9]
h=ls[2]
j=[[70,80]]
ls2=h.extend(j)
print(ls)