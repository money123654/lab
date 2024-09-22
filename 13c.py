from math import *
l=[]
li=[]
st=""
for i in range(3):
    a=int(input("Enter the number : "))
    l.append(a)
print(l)
for i in l:
    qd=sqrt((2*50*i)/30)
    b=int(qd)
    li.append(str(b))
print(li)
st=','.join(li)
print(st)