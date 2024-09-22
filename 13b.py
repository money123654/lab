a=[(10,20,40),(40,50,60),(70,80,100)]
n=int(input("Enter the number : "))
l=[]
for i in a:
    l.append(list(i))
print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][len(l[i])-1]=n
print(l)