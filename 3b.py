from math import *
a=int(input("Enter the 1st integer number : "))
b=int(input("Enter the 2nd integer number : "))
if a%2==1 and b%2==1 and a!=b:
    a,b=b,a
    print("a = ",a,"and b = ",b)
elif a%2==0 and b%2==0 and a!=b:
    if a>b:
        print(a," is largest number")
    else:
        print(b," is largest number")
else:
    print("Factorial of a : ",factorial(a))
    print("Factorial of b : ",factorial(b))