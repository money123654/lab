import re
s=input("Enter the string:")
f=0
k=r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
l=re.search(k,s)
a=s.split(".")
if l:
    for i in a:
        if int(i)>=0 and int(i)<=255:
            f=1 
if f==1:
    print("vlaid")
else:
    print("invalid")
