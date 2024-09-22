s=input("Enter the numbers in binary form which are separated by comma : ")
a=s.split(',')
print(a)
five="0101"
l=[]
for i in a:
    if int(i)%int(five)==0:
        l.append(i)
st=','.join(l)
print(st)