s=input("Enter the string : ")
a=s[:(len(s)+1)//2]
b=s[(len(s))//2:len(s)]
c=s[-1:-(len(s)+1):-1]
print(c)
if a==b and s==c:
    print("String is symmetric and palendromic")
elif a==b and s!=c:
    print("String is symmetric but not palendromic")
elif a!=b and s==c:
    print("String is not symmetric but palendromic")
elif a!=b and s!=c:
    print("String is neither  symmetric nor palendromic")