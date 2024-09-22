n=input("Enter the number : ")
x=int(n)
summ=0
for i in n:
    summ=summ+(int(i)**3)
if summ==x:
    print(x," is an armstrong number")
else:
    print(x," is not an armstrong number")