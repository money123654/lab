import re
s=input("Enter the password : ")
k=r'\b[a-z]+[A-Z]+[0-9]+[$@#]+\b'
if len(s)>=6 and len(s)<=8:
    if re.search(k,s):
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid password")
