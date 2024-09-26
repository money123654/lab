import re
a=open("email.txt","r")
b=open("mail.txt","w")
for i in a:
    k=re.search(r'\b[a-z0-9]+"@"[a-z]{5}"."[a-z]{3}\b',i)
    if k:
        b.write(k.group()+"\n")
a.close()
b.close()