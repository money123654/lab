import re
s=input("Enter the license number : ")
k=r'\b[A-Z]{2}[0-9]{2}[0-9]{4}[0-9]{7}\b'
if re.search(k,s):
    print("Valid license")
else:
    print("Invalid license")

