n=int(input("Enter the value of n : "))
summ=0
res=0
for i in range(1,n+1):
    summ=summ+(1/i)
for i in range(1,n+1):
    res=res+((i**i)/i)   
print(summ)
print(res)