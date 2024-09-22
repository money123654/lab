from math import *
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
qd=b*b-4*a*c
if qd==0:
    print("Roots are real and equal\n")
    r1=-b/(2*a)
    print("Roots : ",r1)
elif qd>0:
    print("Roots are real and distinct\n")
    r1=(-b+(sqrt(qd)))/(2*a)
    r2=(-b-(sqrt(qd)))/(2*a)
    print("Root1 : ",r1)
    print("Root2 : ",r2)
else :
    x=-b/(2*a)
    y=sqrt(abs(qd))/(2*a)
    r1=complex(x,y)
    r2=complex(x,-y)
    print("Root1 : ",r1)
    print("Root2 : ",r2)