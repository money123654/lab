from math import *
n=int(input("Enter the value of n : "))
x=int(input("Enter the value of x : "))
summ=0
sign=1
for i in range(1,n+1,2):
    summ=summ+(((x**i)*sign)/factorial(i))
    sign=sign*-1
print(summ)