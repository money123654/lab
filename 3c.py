n=input("Enter the number : ")
f=0
for i in n:
    if int(n)%int(i)==0:
        f=1
    else:
        f=0
        break
if f==1:
    print(n," is a nude number ")
else :
    print(n," is not a nude number ")