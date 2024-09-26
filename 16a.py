s=input("Enter the string : ")
alp="abcdefghijklmnopqrstuvwxyz"
flag=0
for i in s:
    if i not in alp:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("string is panagram")
else:
    print("string is not panagram")