n=int(input("Enter the size of list : "))
d={}
l=[]
for i in range(n):
    a=int(input("Enter the number : "))
    l.append(a)
print(l)
for i in l:
    d[i]=l.count(i)
print(d)