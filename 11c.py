s=input("Enter the string : ")
st=""
for i in range(len(s)):
    if i==0:
        a=s[i].upper()
        st=st+a+s[1:len(s)-1]
    elif i==len(s)-1:
        b=s[i].upper()
        st=st+b
print(st)