s=input("Enter the words with spaces : ")
a=s.split(" ")
di={}
for i in a:
    di.setdefault(i[0],[])
    di[i[0]].append(i)
print(di)