import re
s=input("Enter the voter ID : ")
k=r'\b[A-Z]+[0-9]+\b'
if len(s)==10:
    if re.search(k,s):
        print("Valid voter ID")
    else:
        print("Invalid voter ID")
else:
    print("Invalid voter ID")