l=[[4,5,6],[2,4,5],[6,7,5]]
for i in range(len(l)):
    li1=[]
    for j in range(len(l[i])-1):
        li=[]
        li.append(l[j])
        li.append(l[2])
    li1.append(list(li))
print(li1)