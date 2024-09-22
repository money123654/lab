l=[(1,2),(2,1),(3,2)]
res=[]
for i in l:
    l.remove(i)
    if i[::-1] in l:
        res.append(i)
if len(res)>0:
    print(res)
else:
    print("No symmetric tuples")