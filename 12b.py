l1=[]
for i in range(3):
    li1=[]
    for j in range(3):
        x=int(input("Enter the number :"))
        li1.append(x)
    print()
    l1.append(li1)
print(l1)
l2=[]
for i in range(3):
    li2=[]
    for j in range(3):
        x=int(input("Enter the number :"))
        li2.append(x)
    print()
    l2.append(li2)
print(l2)
r1=[]
for i in range(3):
    ri1=[]
    x=0
    for j in range(3):
        x+=l1[i][j]*l2[j][i]
        ri1.append(x)
    r1.append(ri1)
print(r1)
