s=input("Enter the number : ")
st=""
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        st=st+s[i]
    if i==len(s)-2:
        st=st+s[-1]
print(st)