s=input("Enter the string : ")
st=""
for i in s:
    if i.isalnum():
        st=st+i
print(st)