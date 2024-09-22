import re
s=input("Enter the string : ")
k=r'\b[A-Z]{4}0[A-Z0-9]{6}\b'
if len(s)==11:
    if re.search(k,s):
        print("Valid IFSC code")
    else:
        print("Invalid IFSC code")
else:
        print("Invalid IFSC code")
  