f=open("F.txt","r")
f1=open("s.txt","r")
f3=open("res.txt","w")
l=f.readlines()
l1=f1.readlines()
for i in range(len(l)):
    j=l[i].replace("\n"," ")
    f3.write(j+l1[i])
f.close()
f1.close()
f3.close() 