from math import *
n=int(input("Enter the odd number of lines : "))
for i in range(n):
    print("*",end=" ",sep=" ")
print()
for j in range(int((n+1)/2)):
    print("   ",end=" ",sep=" ")
    print("*")