def MIRROR_CHARACTER(a):
    st=""
    for i in range(len(a)):
        st=st+(chr(ord('z')-(ord(s[i])-ord('a'))))
    return st

s=input("Enter the string : ")
a=s.lower()
print(MIRROR_CHARACTER(a))