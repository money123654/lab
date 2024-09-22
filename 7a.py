s=input("Enter the string : ")
vow="aeiou"
c=0
if s.isalpha():
    if s.startswith('t') or s.startswith('T'):
        for i in s:
            if i not in vow:
                c=c+1
        print("No. of consonents : ",c)
elif s.isdigit():
    a=s[-1::-1]
    print(a)