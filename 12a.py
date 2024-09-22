s=input("Enter the string : ")
a=s[:(len(s)+1)//2]
b=s[len(s)//2:len(s)]
c=b.upper()
st=""
st=a+c
print(st)