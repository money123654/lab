dic=eval(input("Enter the dictionary : "))
s=input("Enter the string with spaces : ")
a=s.split(" ")
for i in dic:
    if i in a:
        a=s.replace(i,dic[i])
print(a)