import re
s=input("enter string:")
k=r'[A-Z][1-9][0-9]\s?[0-9]{4}[1-9]'
f=0
if len(s)==9 or 8:
   if re.search(k,s):
       f=1
if f==1:
    print("valid") 