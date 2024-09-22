n=input("Enter the number : ")
f=0
for i in range(len(n)):
    if i==0:
        if n[i]=='0':
            f=0
            break
    else:
        if n[i]=='0':
            f=1
            break
        else:
            f=0
if f==1:
    print(n," is duck number")
else:
    print(n," is not duck number")