s=input("Enter the string : ")
ss=input("Enter the substring : ")
st=""
if ss in s:
    nss=input("Enter the new substring : ")
    a=s.replace(ss,nss)
    print(a)
else:
    x=s[:(len(s)+1)//2]
    y=s[(len(s))//2:len(s)]
    st=st+x+ss+y
    print(st)