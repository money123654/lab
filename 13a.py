s1=input("Enter the first sentence with spaces : ")
s2=input("Enter the second sentence with spaces : ")
a=s1.split(' ')
b=s2.split(' ')
st=""
for i in a:
    if i not in b:
        st=st+' '+i
for i in b:
    if i not in a:
        st=st+' '+i
print(st)