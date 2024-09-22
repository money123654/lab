s=input("Enter the string : ")
vow="aeiou"
st=""
for i in s:
    if i not in vow:
        st=st+i
print(st)