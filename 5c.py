from math import *
n=int(input("Enter the value of n : "))
x=int(input("Enter the value of x : "))
summ=1
sign=-1
for i in range(2,n+1,2):
    summ=summ+(((x**i)*sign)/factorial(i))
    sign=sign*-1
print(summ)