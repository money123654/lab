s=input("Enter the string : ")
a=0
n=0
sc=0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        n+=1
    else:
        sc+=1
print("No. of alphabets : ",a)
print("No. of numbers : ",n)
print("No. of special characters : ",sc)