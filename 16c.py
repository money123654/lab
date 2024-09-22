n=int(input("Enter the size of list1 : "))
l1=[]
for i in range(n):
    a=int(input("Enter the number : "))
    l1.append(a)
print(l1)
n1=int(input("Enter the size of list2 : "))
l2=[]
for i in range(n1):
    b=int(input("Enter the number : "))
    l2.append(b)
print(l2)
if l1[0]==l2[-1] and l2[0]==l1[-1]:
    print("Lists are circular")
else:
    print("Lists are not circular")