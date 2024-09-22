s=input("Enter the string with spaces : ")
a=s.split(' ')
print(a)
b=a[-1::-1]
st=' '.join(b)
print(st)